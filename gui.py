import pygame


WIDTH, HEIGHT = 400,200
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
pygame.font.get_init()

def main(caption, question, answer):
    pygame.display.set_caption(caption)
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill((0,179,89))
        display_surface.blit(question, (250,250))
        pygame.display.update()
    pygame.quit()
    # return knew
