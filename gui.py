import pygame

WIDTH, HEIGHT = 400,200
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main(caption, question, answer):
    pygame.display.set_caption(caption)
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

