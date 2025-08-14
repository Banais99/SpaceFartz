import random
import pygame
from circleshape import * 
from constants import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # call parent constructor

    def draw(self, screen):
        # Draw a gray circle at self.position with self.radius, line width 2
        pygame.draw.circle(screen, rand_int, self.position, self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line at constant speed
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2 * 1.2    

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1 * 1.2    