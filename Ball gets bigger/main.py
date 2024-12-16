import sys
from random import Random

import pygame
import random
from pygame import Color
from pygame.time import Clock
from ball import Ball

WIDTH, HEIGHT = 450, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 200

balls = []

clock = Clock()

def drawBall():
    balls.append(Ball(WIDTH/2 + random.randint(-100, 100), HEIGHT/2 + random.randint(-100, 0), 10))

def update():
    for ball in balls:
        ball.move()

        # Calculate distance from the ball to the center of the circle
        distance_to_center = ((ball.x - CENTER[0]) ** 2 + (ball.y - CENTER[1]) ** 2) ** 0.5

        # If the ball is outside the circle, bounce it back
        if distance_to_center + ball.radius > RADIUS:
            ball.radius += 1
            # Calculate the normal vector (from center to ball)
            dx = ball.x - CENTER[0]
            dy = ball.y - CENTER[1]
            magnitude = (dx ** 2 + dy ** 2) ** 0.5

            # Normalize the normal vector
            if magnitude != 0:
                nx = dx / magnitude
                ny = dy / magnitude

                # Reflect the velocity vector
                dot_product = ball.vx * nx + ball.vy * ny
                ball.vx -= 2.02 * dot_product * nx
                ball.vy -= 2.02 * dot_product * ny

                # Slightly move the ball back inside the circle to prevent sticking
                overlap = distance_to_center + ball.radius - RADIUS
                ball.x -= nx * overlap
                ball.y -= ny * overlap





def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawBall()

        # screen.fill((0, 0, 0))

        pygame.draw.circle(screen, Color(255, 255, 255), CENTER, RADIUS, 5)

        update()

        for ball in balls:
            ball.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    try:
        drawBall()
        main()
    finally:
        # Cleanup
        pygame.quit()
        sys.exit()