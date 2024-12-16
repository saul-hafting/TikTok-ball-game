import pygame
import random

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.vy = 1
        self.vx = 0
        self.gravity = 0.15

    def draw(self, screen):

        # Draw the ball
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)

    def move(self):
        self.vy += self.gravity
        self.y += self.vy
        self.x += self.vx
