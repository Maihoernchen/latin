import pygame
# fuckukyle

def main(caption, question, opt1, opt2, opt3, opt4):
    z = len(question)
    WIDTH, HEIGHT = 100+45*z,100+35*z
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.font.init()
    pygame.font.get_init()
    font1 = pygame.font.SysFont('Arial', 40)
    font2 = pygame.font.SysFont('Arial', 20)
    pygame.display.set_caption(caption)
    run=True
    opt1 = "1: " + opt1
    opt2 = "2: " + opt2
    opt3 = "3: " + opt3
    opt4 = "4: " + opt4
    while run:
        text1 = font1.render(question, True, (250, 250, 250))
        text2 = font2.render(opt1, False, (250,250,250))
        text3 = font2.render(opt2, False, (250,250,250))
        text4 = font2.render(opt3, False, (250,250,250))
        text5 = font2.render(opt4, False, (250,250,250))
        WIN.fill((0,179,89))
        WIN.blit(text1, (20,20))
        WIN.blit(text2, (30,70))
        WIN.blit(text3, (30,90))
        WIN.blit(text4, (30,110))
        WIN.blit(text5, (30,130))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    ans = 1
                elif event.key == pygame.K_2:
                    ans = 2
                elif event.key == pygame.K_3:
                    ans = 3
                elif event.key == pygame.K_4:
                    ans = 4
                else:
                    break
                pygame.quit()
                return ans
