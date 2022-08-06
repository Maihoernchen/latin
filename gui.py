import pygame
# fuckukyle

def button(screen, WIDTH, HEIGHT, text):
    if type(text) is list:
        strTemp = ""
        for x in range(len(text)):
            if x == len(text)-1:
                strTemp = strTemp + text[x]
            else:
                strTemp = strTemp + text[x] + ", "
        text = strTemp
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (0, 255, 255))
    x, y, w , h = text_render.get_rect(center=(WIDTH/2,HEIGHT/2))
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (0, 0, 0), (x, y, w , h))
    return screen.blit(text_render, (x, y))

def quit():
    pygame.quit()
def main(caption, question, answers):
    z = len(answers)
    WIDTH, HEIGHT = 1600,100+200*z
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.font.init()
    pygame.font.get_init()
    font1 = pygame.font.SysFont('Arial', 40)
    font2 = pygame.font.SysFont('Arial', 20)
    pygame.display.set_caption(caption)
    run=True
    opt1 = answers[0]
    opt2 = answers[1]
    opt3 = answers[2]
    opt4 = answers[3]
    WIN.fill((0,0,0))
    b1 = button(WIN, WIDTH, 300, opt1)
    b2 = button(WIN, WIDTH, 500, opt2)
    b3 = button(WIN, WIDTH, 700, opt3)
    b4 = button(WIN, WIDTH, 900, opt4)
    while run:
        text1 = font1.render(question, True, (250, 250, 250))
        WIN.blit(text1, (50,50))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        ans = 0
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        ans = 1
                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        ans = 2
                    elif b4.collidepoint(pygame.mouse.get_pos()):
                        ans = 3
                    else:
                        break
                    pygame.quit
                    return ans
        pygame.display.update()
