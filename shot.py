import pygame
from circleshape import * 
from constants import * 

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # Draw a gray circle at self.position with self.radius, line width 2
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line at constant speed
        self.position += self.velocity * dt
