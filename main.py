import pygame
import numpy as np


def setup_screen():
    width = 800
    height = 600
    size = [width, height]
    pygame.display.init()
    pygame.display.set_caption("BennyPaint")
    screen = pygame.display.set_mode(size)
    pixelArray = np.empty(shape=(width, height))
    screen.fill("white")
    pygame.display.update()
    return screen


def main_game_loop(screen):
    playing = True
    clock = pygame.time.Clock()
    down = False
    while playing:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                down = True
            if event.type == pygame.MOUSEBUTTONUP:
                down = False
        if down:
            pos = pygame.mouse.get_pos()
            print(pos)
        screen.fill("white")
        xMax, yMax = screen.get_size()
        menu_rect = pygame.Rect(3*xMax/4, 0, xMax/4, yMax)
        pygame.Surface.fill(screen, color="green", rect=menu_rect)
        #print(screen.get_size())
        pygame.display.update()


if __name__ == '__main__':
    screen = setup_screen()
    main_game_loop(screen)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
