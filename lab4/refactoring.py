import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 800))
rect(screen, (80, 80, 80), (0, 0, 1000, 400))
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
small_cloud_colour1 = [100, 100, 100]
small_cloud_colour2 = [150, 150, 150]
small_cloud_colour3 = [125, 125, 125]
small_cloud_colour4 = [200, 200, 200]
house_colour1 = (60, 82, 45)
house_colour2 = (160, 82, 45)
window_colour1 = (160, 100, 90)
window_colour2 = (255, 255, 90)
balcony_colour1 = (40, 50, 45)
balcony_colour2 = (50, 50, 50)
pipes_colour = (250, 150, 50)
big_cloud_colour1 = (100, 100, 100)
big_cloud_colour2 = (150, 150, 150)
big_cloud_colour3 = (125, 125, 125)
big_cloud_colour4 = (200, 200, 200)

surface_for_big_clouds = pygame.Surface((1000, 800), pygame.SRCALPHA, 32)
surface_for_big_clouds = surface_for_big_clouds.convert_alpha()
surface_for_big_clouds.set_alpha(0)

surface_for_house = pygame.Surface((1000, 800), pygame.SRCALPHA, 32)
surface_for_house = surface_for_house.convert_alpha()
surface_for_house.set_alpha(0)

surface_for_ghost = pygame.Surface((1000, 800), pygame.SRCALPHA, 32)
surface_for_ghost = surface_for_ghost.convert_alpha()
surface_for_ghost.set_alpha(0)

surface_for_small_clouds = pygame.Surface((1000, 800), pygame.SRCALPHA, 32)
surface_for_small_clouds = surface_for_small_clouds.convert_alpha()
surface_for_small_clouds.set_alpha(0)

surfaces = [surface_for_big_clouds, surface_for_house, surface_for_ghost, surface_for_small_clouds]





# moon
circle(screen, white, (700, 100), 100)



# clouds
def big_clouds(surface, x, y):
    '''
    Функция рисует большие облака
    '''
    ellipse(surface, big_cloud_colour1, (x, y, 300, 30))
    ellipse(surface, big_cloud_colour2, (x + 180, y - 20, 400, 50))
    ellipse(surface, big_cloud_colour3, (x + 230, y + 10, 500, 50))
    ellipse(surface, big_cloud_colour4, (x + 480, y + 50, 300, 50))


def small_clouds(surface, alfa, shift_x, shift_y, n):
    '''
    Функция рисует маленькие облака
    surface - поверхность, на которой рисуются маленькие облака
    alfa - коэффициент, меняющий размер маленького облака
    shift_x - абсцисса центра облака
    shift_y - ордината центра облака
    n - прозрачность облака
    '''
    small_cloud_colour1.append(n)
    small_cloud_colour2.append(n)
    small_cloud_colour3.append(n)
    small_cloud_colour4.append(n)
    ellipse(surface, small_cloud_colour1,
            (shift_x + 20, shift_y + 50,
             round(alfa * 300),
             round(alfa * 30)))
    ellipse(surface, small_cloud_colour2,
            (shift_x + 200, shift_y + 30,
             round(alfa * 400),
             round(alfa * 50)))
    ellipse(surface, small_cloud_colour3,
            (shift_x + 250, shift_y + 60,
             round(alfa * 500),
             round(alfa * 50)))
    ellipse(surface, small_cloud_colour4,
            (shift_x + 500, shift_y + 100,
             round(alfa * 300),
             round(alfa * 50)))
    small_cloud_colour1.pop(3)
    small_cloud_colour2.pop(3)
    small_cloud_colour3.pop(3)
    small_cloud_colour4.pop(3)

def house_full(surface, alfa, shift_x, shift_y, n):
    '''
    surface - поверхность, на которой рисуется дом
    alfa - коэффициент, меняющий размер дома
    shift_x - абсцисса верхнего левого угла дома
    shift_y - ордината верхнего левого угла дома
    n - прозрачность дома
    '''
    house(surface, alfa, shift_x, shift_y, n)
    windows(surface, alfa, shift_x, shift_y, n)
    balcony(surface, alfa, shift_x, shift_y, n)
    pipes(surface, alfa, shift_x, shift_y, n)


def house(surface, alfa, shift_x, shift_y, n):
    '''
    surface - поверхность, на которой рисуется дом
    alfa - коэффициент, меняющий размер дома
    shift_x - абсцисса верхнего левого угла дома
    shift_y - ордината верхнего левого угла дома
    n - прозрачность дома
    '''
    right = 330

    rect(surface, house_colour2,
         (round(shift_x + alfa * 30),
          round(shift_y + alfa * 200),
          round(alfa * right),
          round(alfa * 600)))
    s = pygame.Surface((round(alfa * right),
                        round(alfa * 600)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s,
                ((round(shift_x + alfa * 30)),
                round(shift_y + alfa * 200))
                )
    for i in range(4):
        rect(surface, house_colour1, (
            round(shift_x + alfa * 50 + i * alfa * 70),
            round(shift_y + alfa * 200),
            round(alfa * 50),
            round(alfa * 300)))
        s = pygame.Surface((round(alfa * 50), round(alfa * 300)))
        s.set_alpha(n)
        s.fill(white)
        surface.blit(s,
                    (round(shift_x + alfa * 50 + i * alfa * 70),
                    round(shift_y + alfa * 200)))


def windows(surface, alfa, shift_x, shift_y, n):
    '''
    surface - поверхность, на которой рисуются окна дом
    alfa - коэффициент, меняющий размер окна
    shift_x - абсцисса верхнего левого угла дома
    shift_y - ордината верхнего левого угла дома
    n - прозрачность окна
    '''
    x_window = alfa * 50
    y_window = alfa * 700
    x_plus = alfa * 50
    y_plus = alfa * 60
    x_step = alfa * 100

    rect(surface,
         window_colour1,
         (round(shift_x + x_window),
         round(shift_y + y_window),
         round(x_plus),
         round(y_plus)))
    s = pygame.Surface((round(x_plus), round(y_plus)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s, (round(shift_x + x_window),
                    round(shift_y + y_window)))
    rect(surface,
         window_colour1,
         (round(shift_x + x_window + x_step),
          round(shift_y + y_window),
          round(x_plus),
          round(y_plus)))
    s = pygame.Surface((round(x_plus), round(y_plus)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s,
                (round(shift_x + x_window + x_step),
                round(shift_y + y_window)))
    rect(surface, window_colour2,
         (round(shift_x + x_window + 2 * x_step),
          round(shift_y + y_window),
          round(x_plus),
          round(y_plus)))
    s = pygame.Surface((round(x_plus),
                        round(y_plus)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s, (round(shift_x + x_window + 2 * x_step),
                    round(shift_y + y_window)))


def balcony(surface, alfa, shift_x, shift_y, n):
    '''
    surface - поверхность, на которой рисуется балкон дом
    alfa - коэффициент, меняющий размер балкона
    shift_x - абсцисса верхнего левого угла дома
    shift_y - ордината верхнего левого угла дома
    n - прозрачность балкона
    '''

    right = 330
    y_window = alfa * 700
    rect(surface,
         balcony_colour1,
         (round(shift_x + 0),
          round(shift_y + y_window - 200 * alfa),
          round(alfa * (right + 60)),
          round(alfa * 30)))
    s = pygame.Surface((round(alfa * (right + 60)),
                        round(alfa * 30)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s,
                (round(shift_x + 0),
                round(shift_y + y_window - 200 * alfa)))
    rect(surface, balcony_colour1, (
        round(shift_x + alfa * 20),
        round(shift_y + y_window - alfa * 250),
        round(alfa * (right + 20)),
        round(alfa * 20)))
    s = pygame.Surface((round(alfa * (right + 20)),
                        round(alfa * 20)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s, (round(shift_x + alfa * 20),
                    round(shift_y + y_window - alfa * 250)))
    rect(surface, balcony_colour1,
         (round(shift_x + alfa * 10),
          round(shift_y + y_window - alfa * 250),
          round(alfa * 10),
          round(alfa * 50)))
    s = pygame.Surface((round(alfa * 10),
                        round(alfa * 50)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s,
                (round(shift_x + alfa * 10),
                round(shift_y + y_window - alfa * 250)))
    for i in range(5):
        rect(surface, balcony_colour1, (
            round(shift_x + alfa * 10 + (i + 1) * alfa * 60),
            round(shift_y + y_window - alfa * 250),
            round(alfa * 20),
            round(alfa * 50)))
        s = pygame.Surface((round(alfa * 20),
                            round(alfa * 50)))
        s.set_alpha(n)
        s.fill(white)
        surface.blit(s,
                    (round(shift_x + alfa * 10 + (i + 1) * alfa * 60),
                    round(shift_y + y_window - alfa * 250)))
    rect(surface, balcony_colour1, (
        round(shift_x + alfa * (right + 40)),
        round(shift_y + y_window - alfa * 250),
        round(alfa * 10),
        round(alfa * 50)))
    s = pygame.Surface((round(alfa * 10),
                        round(alfa * 50)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s,
                (round(shift_x + alfa * (right + 40)),
                round(shift_y + y_window - alfa * 250)))
    polygon(surface,
            balcony_colour2,
            [
            [round(shift_x + 0), round(shift_y + alfa * 200)],
            [round(shift_x + alfa * (right + 60)), round(shift_y + alfa * 200)],
            [round(shift_x + alfa * (right + 30)), round(shift_y + alfa * 160)],
            [round(shift_x + 0 + alfa * 30), round(shift_y + alfa * 160)]
            ]
            )


def pipes(surface, alfa, shift_x, shift_y, n):
    '''
    surface - поверхность, на которой рисуются трубы дом
    alfa - коэффициент, меняющий размер трубы
    shift_x - абсцисса верхнего левого угла дома
    shift_y - ордината верхнего левого угла дома
    n - прозрачность трубы
    '''
    rect(surface,
         pipes_colour,
         (round(shift_x + alfa * 100),
          round(shift_y + alfa * 90),
          round(alfa * 20),
          round(alfa * 100)))
    s = pygame.Surface((round(alfa * 20),
                        round(alfa * 100)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s,
                (round(shift_x + alfa * 100),
                round(shift_y + alfa * 90)))
    rect(surface, pipes_colour,
         (round(shift_x + alfa * 80),
          round(shift_y + alfa * 90),
          round(alfa * 10),
          round(alfa * 90)))
    s = pygame.Surface((round(alfa * 10),
                        round(alfa * 90)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s,
                (round(shift_x + alfa * 80),
                round(shift_y + alfa * 90)))
    rect(surface, pipes_colour,
         (round(shift_x + alfa * 230),
          round(shift_y + alfa * 120),
          round(alfa * 10),
          round(alfa * 50)))
    s = pygame.Surface((round(alfa * 10),
                        round(alfa * 50)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s,
                (round(shift_x + alfa * 230),
                round(shift_y + alfa * 120)))
    rect(surface, pipes_colour,
         (round(shift_x + alfa * 300),
          round(shift_y + alfa * 90),
          round(alfa * 10),
          round(alfa * 80)))
    s = pygame.Surface((round(alfa * 10),
                        round(alfa * 80)))
    s.set_alpha(n)
    s.fill(white)
    surface.blit(s,
                (round(shift_x + alfa * 300),
                round(shift_y + alfa * 90)))


def ghost(surface, x_ghost, y_ghost, size):
    '''
    surface - поверхность, на которой рисуются призраки
    x_ghost - абсцисса опорной точки призрака
    y_ghost - ордината опорной точки призрака
    size - отвечает за ориентацию призрака,
        если < 0 то ориентирован влево,
        если > 0 nj ориентирован вправо
    '''
    polygon(surface,
            white,
            [[x_ghost, y_ghost],
            [x_ghost + size * 50, y_ghost + 45],
            [x_ghost + size * 60, y_ghost + 50],
            [x_ghost + size * 70, y_ghost + 55],
            [x_ghost + size * 75, y_ghost + 65],
            [x_ghost + size * 80, y_ghost + 70],
            [x_ghost + size * 90, y_ghost + 80],
            [x_ghost + size * 100, y_ghost + 90],
            [x_ghost + size * 115, y_ghost + 110],
            [x_ghost + size * 100, y_ghost + 110],
            [x_ghost + size * 115, y_ghost + 120],
            [x_ghost + size * 130, y_ghost + 125],
            [x_ghost + size * 140, y_ghost + 130],
            [x_ghost + size * 100, y_ghost + 130],
            [x_ghost + size * 80, y_ghost + 127],
            [x_ghost + size * 60, y_ghost + 120],
            [x_ghost + size * 30, y_ghost + 130],
            [x_ghost + size * 25, y_ghost + 127],
            [x_ghost + size * 20, y_ghost + 120],
            [x_ghost - size * 8, y_ghost + 122],
            [x_ghost - size * 15, y_ghost + 124],
            [x_ghost - size * 20, y_ghost + 127],
            [x_ghost - size * 30, y_ghost + 130],
            [x_ghost - size * 60, y_ghost + 100],
            [x_ghost - size * 50, y_ghost + 80],
            [x_ghost - size * 40, y_ghost + 65],
            [x_ghost - size * 30, y_ghost + 60],
            [x_ghost, y_ghost]])
    circle(surface, white, (x_ghost, y_ghost), 30)
    circle(surface, blue, (x_ghost - 10, y_ghost - 5), 7)
    circle(surface, blue, (x_ghost + 10, y_ghost - 5), 7)
    circle(surface, red, (x_ghost - 10, y_ghost - 5), 3)
    circle(surface, red, (x_ghost + 10, y_ghost - 5), 3)
    ellipse(surface, black, (x_ghost - 7, y_ghost + 7, 20, 20))



house_full(surface_for_house, 0.3, 500, 300, 200)
small_clouds(surface_for_small_clouds, 0.3, 500, 300, 200)
house_full(surface_for_house, 0.4, 250, 400, 100)
small_clouds(surface_for_small_clouds, 0.4, 250, 400, 100)
house_full(surface_for_house, 0.5, 0, 600, 50)
small_clouds(surface_for_small_clouds, 0.4, 250, 400, 100)
big_clouds(surface_for_big_clouds, 20 ,50)
ghost(surface_for_ghost, 500, 500, 1)
ghost(surface_for_ghost, 250, 300, -1)
ghost(surface_for_ghost, 500, 750, 1)
ghost(surface_for_ghost, 450, 200, -1)
ghost(surface_for_ghost, 370, 660, 1)
ghost(surface_for_ghost, 700, 370, -1)

#наложение всех поверхностей
for i in surfaces:
    screen.blit(i, (0, 0))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
