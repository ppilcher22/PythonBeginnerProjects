import pygame, sys

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
LINE_COLOUR = (23, 145, 135)
RED = (255,0,0)
BG_COLOUR = (28,170,156)

screen = pygame.display.set_mode( (WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOUR)

def draw_lines():
    pygame.draw.line(screen, LINE_COLOUR, (0,200), (600,200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0,400), (600,400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (200,0), (200,600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (400,0), (400,600), LINE_WIDTH)

draw_lines()
rect_1 = pygame.draw.rect(screen, LINE_COLOUR, (200,150,100,50))

#mainloop
while True:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = rect_1.collidepoint(pygame.mouse.get_pos())
            if click == 1:
                print('inside')
            

    pygame.display.update()