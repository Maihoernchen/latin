import pygame
# fuckukyle

def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))

def main(caption, question, answers):
    z = len(question)
    WIDTH, HEIGHT = 100+45*z,100+35*z
    WIN = pygame.display.set_mode((1620, 960))
    pygame.font.init()
    pygame.font.get_init()
    font1 = pygame.font.SysFont('Arial', 40)
    font2 = pygame.font.SysFont('Arial', 20)
    pygame.display.set_caption(caption)
    run=True
    opt1 = "1: " + answers[0]
    opt2 = "2: " + answers[1]
    opt3 = "3: " + answers[2]
    opt4 = "4: " + answers[3]
    WIN.fill((0,0,0))
    b1 = button(WIN, (0, 300), opt1)
    b2 = button(WIN, (0, 400), opt2)
    b3 = button(WIN, (0, 500), opt3)
    b4 = button(WIN, (0, 600), opt4)
    while run:
        text1 = font1.render(question, True, (250, 250, 250))
        text2 = font2.render(opt1, False, (250,250,250))
        text3 = font2.render(opt2, False, (250,250,250))
        text4 = font2.render(opt3, False, (250,250,250))
        text5 = font2.render(opt4, False, (250,250,250))
        WIN.blit(text1, (50,50))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if key_to_start:
                    print("okay lets goo")
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        ans = 1
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        ans = 2
                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        ans = 3
                    elif b4.collidepoint(pygame.mouse.get_pos()):
                        ans = 4
                    else:
                        break
                    pygame.quit
                    return ans
        pygame.display.update()
