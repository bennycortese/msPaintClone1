import pygame


def setup_screen():
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    screen.fill("white")
    pygame.display.update()
    pygame.display.set_caption("BennyPaint")
    return screen


def main_game_loop(screen):
    playing = True
    clock = pygame.time.Clock()
    while playing:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        screen.fill("white")
        pygame.display.update()


if __name__ == '__main__':
    screen = setup_screen()
    main_game_loop(screen)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
