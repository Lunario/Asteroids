import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        x_vel = self.velocity.x
        y_vel = self.velocity.y
        self.position[0] += x_vel * dt
        self.position[1] += y_vel * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rot = random.uniform(20, 50)
        new_vel = self.velocity * 1.2
        vel1 = new_vel.rotate(rot)
        vel2 = new_vel.rotate(-rot)

        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        

        child1 = Asteroid(self.position[0], self.position[1], new_radius)
        child2 = Asteroid(self.position[0], self.position[1], new_radius)
        child1.velocity = vel1
        child2.velocity = vel2