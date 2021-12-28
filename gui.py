import pygame


WIDTH, HEIGHT = 400,200
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
pygame.font.init()
pygame.font.get_init()

def main(caption, question, answer):
    pygame.display.set_caption(caption)
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        text1 = font1.render(question, True, (0, 255, 0))
        WIN.fill((0,179,89))
        WIN.blit(text1, (250,250))
        pygame.display.update()
    pygame.quit()
    # return knew
