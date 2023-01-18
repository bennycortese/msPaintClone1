import pygame
import numpy as np
import copy


def setup_screen(width, height):
    size = [width, height]
    pygame.display.init()
    pygame.display.set_caption("BennyPaint")
    screen = pygame.display.set_mode(size)
    screen.fill("white")
    pygame.display.update()
    return screen


def increase_pixel_size(positions_altered):
    color = None
    result_dict = dict()
    for position in positions_altered:
        color = positions_altered[position]
        result_dict[(position[0], position[1])] = color
        result_dict[(position[0], position[1] - 1)] = color
        result_dict[(position[0] - 1, position[1])] = color
        result_dict[(position[0], position[1] + 1)] = color
        result_dict[(position[0] + 1, position[1])] = color
        result_dict[(position[0] + 1, position[1] - 1)] = color
        result_dict[(position[0] - 1, position[1] + 1)] = color
        result_dict[(position[0] - 1, position[1] - 1)] = color
        result_dict[(position[0] + 1, position[1] + 1)] = color
    return result_dict


def num_key_map():
    num_map = dict()
    num_map[pygame.K_1] = 1
    num_map[pygame.K_2] = 2
    num_map[pygame.K_3] = 3
    num_map[pygame.K_4] = 4
    num_map[pygame.K_5] = 5
    num_map[pygame.K_6] = 6
    num_map[pygame.K_7] = 7
    num_map[pygame.K_8] = 8
    num_map[pygame.K_9] = 9
    return num_map

def color_map():
    color_mapping = dict()
    color_mapping["black"] = [0, 0, 0]
    color_mapping["red"] = [255, 0, 0]
    color_mapping["green"] = [0, 255, 0]
    color_mapping["blue"] = [0, 0, 255]
    color_mapping["yellow"] = [255, 255, 0]
    color_mapping["white"] = [255, 255, 255]
    color_mapping["cyan"] = [0, 255, 255]
    color_mapping["orange"] = [255, 165, 0]
    color_mapping["celeste_sky_blue"] = [178, 255, 255]
    color_mapping["pink"] = [255, 192, 203]
    return color_mapping

def main_game_loop(screen, width, height):
    pixelArray = np.zeros([height, int((width / 4) * 3), 3], dtype=np.uint8)
    for i in range(len(pixelArray)):
        for j in range(len(pixelArray[i])):
            pixelArray[i][j] = (255, 255, 255)
    color_mapping = color_map()
    print(len(pixelArray[0]))
    playing = True
    clock = pygame.time.Clock()
    down = False
    positions_altered = dict()
    clock.tick(60)
    draw_color = "black"
    pixel_size = 3
    num_map = num_key_map()
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                xMax, yMax = screen.get_size()
                if pos[0] > 3 * xMax / 4:
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
                if event.key == pygame.K_c:
                    draw_color = "cyan"
                if event.key == pygame.K_o:
                    draw_color = "orange"
                if event.key == pygame.K_s:
                    draw_color = "celeste_sky_blue"
                if event.key == pygame.K_p:
                    draw_color = "pink"
                if event.key in num_map:
                    pixel_size = num_map[event.key]
        if down:
            pos = pygame.mouse.get_pos()
            temp_dict = dict()
            temp_dict[(pos[0], pos[1])] = draw_color
            for i in range(pixel_size - 1):
                temp_dict = increase_pixel_size(temp_dict)
            positions_altered.update(temp_dict)
        for position in positions_altered:
            pixelArray[position[0]][position[1]] = color_mapping[positions_altered[position]]
            screen.set_at(position, color_mapping[positions_altered[position]])
        positions_altered.clear()
        xMax, yMax = screen.get_size()
        menu_rect = pygame.Rect(3 * xMax / 4, 0, xMax / 4, yMax)
        pygame.Surface.fill(screen, color="green", rect=menu_rect)
        # print(screen.get_size())
        pygame.display.update()


if __name__ == '__main__':
    width = 800
    height = 600
    screen = setup_screen(width, height)
    main_game_loop(screen, width, height)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
