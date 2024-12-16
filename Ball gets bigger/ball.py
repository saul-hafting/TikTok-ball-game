import pygame
import random

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.c1 = random.randint(0, 255)
        self.c2 = random.randint(0, 255)
        self.c3 = random.randint(0, 255)
        self.c1_direction = 1  # Direction of color change (+1 or -1)
        self.c2_direction = 1
        self.c3_direction = 1
        self.vy = 1
        self.vx = 0
        self.gravity = 0.5

    def draw(self, screen):
        # Update color components gradually and reverse direction if limits are hit
        if self.c1 >= 255 or self.c1 <= 0:
            self.c1_direction *= -1
        if self.c2 >= 255 or self.c2 <= 0:
            self.c2_direction *= -1
        if self.c3 >= 255 or self.c3 <= 0:
            self.c3_direction *= -1

        self.c1 += self.c1_direction
        self.c2 += self.c2_direction
        self.c3 += self.c3_direction

        # Draw the ball
        pygame.draw.circle(screen, (self.c1, self.c2, self.c3), (self.x, self.y), self.radius)
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius, width=2)

    def move(self):
        self.vy += self.gravity
        self.y += self.vy
        self.x += self.vx
