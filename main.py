import pygame
import numpy as np
import copy
import random


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
    color_mapping["grey"] = [128, 128, 128]
    color_mapping["fuchsia"] = [255, 0, 255]
    color_mapping["emerald_green"] = [80, 200, 120]
    color_mapping["some_green"] = [120, 240, 140]
    color_mapping["random"] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    color_mapping["gold"] = [255, 215, 0]
    return color_mapping


def main_game_loop(screen, width, height):
    draw_mode = "pixel"
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
                if event.key == pygame.K_g:
                    draw_color = "grey"
                if event.key == pygame.K_f:
                    draw_color = "fuchsia"
                if event.key == pygame.K_e:
                    draw_color = "emerald_green"
                if event.key == pygame.K_r:
                    draw_color = "random"
                    color_mapping["random"] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                if event.key == pygame.K_s:
                    draw_mode = "bucket"
                if event.key in num_map:
                    pixel_size = num_map[event.key]
        if down and draw_mode == "pixel":
            pos = pygame.mouse.get_pos()
            temp_dict = dict()
            temp_dict[(pos[0], pos[1])] = draw_color
            for i in range(pixel_size - 1):
                temp_dict = increase_pixel_size(temp_dict)
            positions_altered.update(temp_dict)
        if down and draw_mode == "bucket":
            pos = pygame.mouse.get_pos()
            temp_dict = dict()
            temp_dict = fill_bucket(pos, pixelArray, color_mapping, draw_color, temp_dict, 0)
            positions_altered.update(temp_dict)
        for position in positions_altered:
            if position[0] < 3 * xMax / 4:
                pixelArray[position[0]][position[1]] = color_mapping[positions_altered[position]]
                screen.set_at(position, color_mapping[positions_altered[position]])
        positions_altered.clear()
        xMax, yMax = screen.get_size()
        menu_rect = pygame.Rect(3 * xMax / 4, 0, xMax / 4, yMax)
        pygame.Surface.fill(screen, color="green", rect=menu_rect)
        # print(screen.get_size())
        pygame.display.update()


def fill_bucket(position, pixelArray, color_mapping, draw_color, replace_values, count):
    if 0 < position[0] < 400 and 400 > position[1] > 0:
        changedColor = np.array(color_mapping[draw_color])
        if not np.array_equal(pixelArray[position[0]][position[1]], changedColor) and count < 5:
            count += 1;
            replace_values[position] = draw_color
            pixelArray[position[0]][position[1]] = color_mapping[draw_color]
            fill_bucket((position[0] + 1, position[1]), pixelArray, color_mapping, draw_color, replace_values, count)
            fill_bucket((position[0] - 1, position[1]), pixelArray, color_mapping, draw_color, replace_values, count)
            fill_bucket((position[0], position[1] + 1), pixelArray, color_mapping, draw_color, replace_values, count)
            fill_bucket((position[0], position[1] - 1), pixelArray, color_mapping, draw_color, replace_values, count)
    return replace_values


if __name__ == '__main__':
    width = 800
    height = 600
    screen = setup_screen(width, height)
    main_game_loop(screen, width, height)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
