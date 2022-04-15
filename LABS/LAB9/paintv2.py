import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

finished = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221, 160, 221)

# creating rectangle
def drawRect(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

# creating circle
def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

# creating square
def drawSquare(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, width))

# creating rhombus
def drawRhombus(color, pos1, pos2):
    pygame.draw.lines(screen, color, True, (((pos1[0]+pos2[0])/2, pos1[1]), (pos1[0], (pos1[1]+pos2[1])/2), ((
        pos1[0]+pos2[0])/2, pos2[1]), (pos2[0], (pos1[1]+pos2[1])/2)), 5)

# creating equilaterial triangle
def drawEqui(color, pos1, pos2):
    widthb = abs(pos2[0]-pos1[0])
    heightp = (3**0.5)*widthb/2
    if pos2[1] > pos1[1]:
        pygame.draw.polygon(screen, color, ((pos1[0], pos2[1]), (pos2[0], pos2[1]), ((
            pos1[0]+pos2[0])/2, pos2[1]-heightp)), 5)
    else:
        pygame.draw.polygon(screen, color, ((pos1[0], pos1[1]), (pos2[0], pos1[1]), ((
            pos1[0]+pos2[0])/2, pos1[1]-heightp)), 5)

# creating right triangle
def drawRight(color, pos1, pos2):
    if pos2[0] > pos1[0] and pos2[1] > pos1[1]:
        pygame.draw.polygon(
            screen, color, ((pos1[0], pos1[1]), (pos2[0], pos2[1]), (pos1[0], pos2[1])), 5)
    if pos2[1] > pos1[1] and pos1[0] > pos2[0]:
        pygame.draw.polygon(
            screen, color, ((pos1[0], pos1[1]), (pos2[0], pos2[1]), (pos1[0], pos2[1])), 5)
    if pos1[0] > pos2[0] and pos1[1] > pos2[1]:
        pygame.draw.polygon(
            screen, color, ((pos1[0], pos1[1]), (pos2[0], pos2[1]), (pos2[0], pos1[1])), 5)
    if pos2[0] > pos1[0] and pos1[1] > pos2[1]:
        pygame.draw.polygon(
            screen, color, ((pos1[0], pos1[1]), (pos2[0], pos2[1]), (pos2[0], pos1[1])), 5)

# creating eraser
def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

RAD = 30

drawing = False
color = BLACK

screen.fill(pygame.Color('white'))

start_pos = 0
end_pos = 0

mode = 0

all_colors = []

# creating range of colors
for _ in range(20):
    all_colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))

# main loop
while not finished:
    clock.tick(FPS)
    pos = pygame.mouse.get_pos()  # getting the position of the mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # getting starting position when mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pos
            if pos[0] > 20 and pos[0] < 720 and pos[1] > 20 and pos[1] < 40:
                color = screen.get_at(pos)
        # releasing mouse click
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pos
            rect_x = abs(start_pos[0] - end_pos[0])
            rect_y = abs(start_pos[1] - end_pos[1])

            # calling the functions
            if mode == 0:
                drawRect(color, start_pos, rect_x, rect_y)
            if mode == 1:
                drawCircle(color, start_pos, rect_x)
            if mode == 3:
                drawSquare(color, start_pos, rect_x, rect_y)
            if mode == 4:
                drawRhombus(color, start_pos, end_pos)
            if mode == 5:
                drawEqui(color, start_pos, end_pos)
            if mode == 6:
                drawRight(color, start_pos, end_pos)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == 2:  # 2 is for eraser
                eraser(pos, RAD)

        # changing tool with "space" button
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         mode += 1
        #         mode %= 3

        # pressing buttons to change tools
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # rectangle
                mode = 0
            if event.key == pygame.K_2:  # circle
                mode = 1
            if event.key == pygame.K_3:  # eraser
                mode = 2
            if event.key == pygame.K_4:  # square
                mode = 3
            if event.key == pygame.K_5:  # rhombus
                mode = 4
            if event.key == pygame.K_6:  # equilateral triangle
                mode = 5
            if event.key == pygame.K_7:
                mode = 6
            if event.key == pygame.K_BACKSPACE: # clears the entire window
                screen.fill(pygame.Color('white'))
   
    # drawing blocks of colors
    each = 35
    for i, col in enumerate(all_colors):
        pygame.draw.rect(screen, col, (20 + i * each, 20, each, 20))
    pygame.display.flip()
pygame.quit()
