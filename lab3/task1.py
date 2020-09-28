import pygame
from pygame.draw import *

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
brown = (150, 75, 0)
FPS = 30
screen = pygame.display.set_mode((500, 500))
rect(screen, white, (0, 0, 500, 500))


def face(x_center, y_center, radius):
    circle(screen, black, (x_center, y_center), radius + 5, 5)
    circle(screen, yellow, (x_center, y_center), radius)
    rect(screen, black, (150, 250, 100, 20))


def eyes(x_center, y_center, radius):
    circle(screen,
           red,
           (round(x_center - radius / 2),
            round(y_center - radius / 2)),
            round(radius / 5))
    circle(screen,
           red,
           (round(x_center + radius / 2),
            round(y_center - radius / 2)),
            round(radius / 5))
    circle(screen,
           black,
           (round(x_center - radius / 2),
           round(y_center - radius / 2)),
           round(radius / 10))
    circle(screen,
           black,
           (round(x_center + radius / 2),
           round(y_center - radius / 2)),
           round(radius / 10))


def eyebrows(x_center, y_center, radius):
    polygon(screen,
            brown,
            [
             [x_center - 0.7 * radius, y_center - radius],
             [x_center - 0.6 * radius, y_center - 1.1 * radius],
             [x_center - 0.1 * radius, y_center - 0.5 * radius],
             [x_center - 0.2 * radius, y_center - 0.4 * radius]])
    polygon(screen, brown,
            [[x_center + 0.7 * radius, y_center - radius],
             [x_center + 0.6 * radius, y_center - 1.1 * radius],
             [x_center + 0.1 * radius, y_center - 0.5 * radius],
             [x_center + 0.2 * radius, y_center - 0.4 * radius]])


def smile(x_center, y_center, radius):
    face(x_center, y_center, radius)
    eyes(x_center, y_center, radius)
    eyebrows(x_center, y_center, radius)


smile(200, 200, 100)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
