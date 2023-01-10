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
    positions_altered = dict()
    clock.tick(300)
    draw_color = "black"
    pixel_size = 2
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                xMax, yMax = screen.get_size()
                if pos[0] > 3*xMax/4:
                    positions_altered.clear()
                    screen.fill(color="white")
                down = True
            if event.type == pygame.MOUSEBUTTONUP:
                down = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    draw_color = "blue"
                if event.key == pygame.K_r:
                    draw_color = "red"
                if event.key == pygame.K_y:
                    draw_color = "yellow"
                if event.key == pygame.K_g:
                    draw_color = "green"
                if event.key == pygame.K_w:
                    draw_color = "white"
                if event.key == pygame.K_u:
                    draw_color = "black"
                if event.key == pygame.K_3:
                    pixel_size = 3
                if event.key == pygame.K_2:
                    pixel_size = 2
        if down:
            pos = pygame.mouse.get_pos()
            positions_altered[(pos[0], pos[1])] = draw_color
            positions_altered[(pos[0] + 1, pos[1])] = draw_color
            positions_altered[(pos[0], pos[1] + 1)] = draw_color
            positions_altered[(pos[0] - 1, pos[1])] = draw_color
            positions_altered[(pos[0], pos[1] - 1)] = draw_color
            positions_altered[(pos[0] - 1, pos[1] - 1)] = draw_color
            positions_altered[(pos[0] + 1, pos[1] - 1)] = draw_color
            positions_altered[(pos[0] + 1, pos[1] + 1)] = draw_color
            positions_altered[(pos[0] - 1, pos[1] + 1)] = draw_color
            if pixel_size == 3:
                positions_altered[(pos[0], pos[1] + 2)] = draw_color
                positions_altered[(pos[0] + 1, pos[1] + 2)] = draw_color
                positions_altered[(pos[0] - 1, pos[1] + 2)] = draw_color
                positions_altered[(pos[0], pos[1] - 2)] = draw_color
                positions_altered[(pos[0] - 1, pos[1] - 2)] = draw_color
                positions_altered[(pos[0] + 1, pos[1] - 2)] = draw_color
                positions_altered[(pos[0] + 2, pos[1])] = draw_color
                positions_altered[(pos[0] + 2, pos[1] - 1)] = draw_color
                positions_altered[(pos[0] + 2, pos[1] + 1)] = draw_color
                positions_altered[(pos[0] - 2, pos[1])] = draw_color
                positions_altered[(pos[0] - 2, pos[1] - 1)] = draw_color
                positions_altered[(pos[0] - 2, pos[1] + 1)] = draw_color

                positions_altered[(pos[0] + 2, pos[1] + 2)] = draw_color
                positions_altered[(pos[0] - 2, pos[1] + 2)] = draw_color
                positions_altered[(pos[0] + 2, pos[1] - 2)] = draw_color
                positions_altered[(pos[0] - 2, pos[1] - 2)] = draw_color

        for position in positions_altered:
            screen.set_at(position, positions_altered[position])
        xMax, yMax = screen.get_size()
        menu_rect = pygame.Rect(3*xMax/4, 0, xMax/4, yMax)
        pygame.Surface.fill(screen, color="green", rect=menu_rect)
        #print(screen.get_size())
        pygame.display.update()


if __name__ == '__main__':
    screen = setup_screen()
    main_game_loop(screen)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
