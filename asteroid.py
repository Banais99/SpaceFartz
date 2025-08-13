import pygame
from circleshape import * 
from constants import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # call parent constructor

    def draw(self, screen):
        # Draw a gray circle at self.position with self.radius, line width 2
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line at constant speed
        self.position += self.velocity * dt
