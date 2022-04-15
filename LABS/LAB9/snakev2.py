import pygame
import time
from random import randint, randrange


pygame.init()

WIDTH = 800
HEIGHT = 800
FPS = 10
cell = 40

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (221, 160, 221)

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE")
score_font = ("Arial", 40)

finished = False

clock = pygame.time.Clock()

t = 0

font = pygame.font.SysFont("Arial", 40)

# creating food
class Food:
    def __init__(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)

    # creating initial food
    def draw(self):
            pygame.draw.rect(screen, RED, (self.x, self.y, cell, cell))

    # creating new food
    def redraw(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)


# creating borders
class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        pygame.draw.rect(screen, PURPLE, (self.x, self.y, cell, cell))

# creating a snake


class Snake:
    def __init__(self):
        self.speed = cell
        self.body = [[80, 80], [1000, 1000], [
            1040, 1040], [1080, 1080], [1120, 1120]]
        self.dx = self.speed
        self.dy = 0
        self.direction = ''
        self.color = GREEN

    # logic of movement
    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.direction != "right":
                    self.dx = -self.speed
                    self.dy = 0
                    self.direction = "left"
                if event.key == pygame.K_d and self.direction != "left":
                    self.dx = self.speed
                    self.dy = 0
                    self.direction = "right"
                if event.key == pygame.K_w and self.direction != "down":
                    self.dx = 0
                    self.dy = -self.speed
                    self.direction = "up"
                if event.key == pygame.K_s and self.direction != "up":
                    self.dx = 0
                    self.dy = self.speed
                    self.direction = "down"

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        # going from right side to left and from left to right and from top to bottom and from bottom to top
        if self.body[0][0] > WIDTH:
            self.body[0][0] = 0

        if self.body[0][1] > HEIGHT:
            self.body[0][1] = 0

        if self.body[0][0] < 0:
            self.body[0][0] = WIDTH

        if self.body[0][1] < 0:
            self.body[0][1] = HEIGHT

        # self.body[0][0] % WIDTH
        # self.body[0][1] %= HEIGHT

    # drawing the snake
    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color,
                             (block[0], block[1], cell, cell))

    # eating an apple
    def collide_food(self, f: Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            self.body.append([1000, 1000])

    # death
    def collide_self(self):
        global finished, lose
        if self.body[0] in self.body[1:]:
            lose = True

    # creating new apple
    def check_food(self, f: Food):
        if [f.x, f.y] in self.body:
            f.redraw()
            global SCORE
            SCORE += randint(1, 3) # random weight

s = Snake()
f = Food()

SCORE = 0
lose = False
level = 0


while not finished:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            finished = True # closing the window with "X" and "esc" button
        # switching to next levels depending on score
        if SCORE >= 3:
            FPS = 12 # increasing speed
            level = 1
        if SCORE >= 7:
            FPS = 13
            level = 2
    
    # filling background
    screen.fill(WHITE)

    # initalizing walls with txt files
    walls_coor = open(f"wall{level}.txt", "r").readlines()

    walls = []

    # creating walls
    for i, line in enumerate(walls_coor):
        for j, each in enumerate(line):
            if each == "#":
                walls.append(Wall(j * cell, i * cell))

    # loop for window not to close after death and display "Game Over!"
    while lose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = not finished
                lose = not lose
        go_font = pygame.font.SysFont("Arial", 40)
        go_img = go_font.render("Game Over!", True, BLACK)
        screen.blit(go_img, go_img.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()

    f.draw()
    s.draw()
    s.move(events)
    s.collide_food(f)
    s.collide_self()
    s.check_food(f)

    for wall in walls:
        wall.draw()
        if f.x == wall.x and f.y == wall.y:
            f.redraw()

        if s.body[0][0] == wall.x and s.body[0][1] == wall.y:
            lose = True

    # respawn of apple
    t += FPS % 3
    if t % 70 == 0 and t > 0:
        f.redraw()

    # displaying score
    score_font = pygame.font.SysFont("Arial", 40)
    score_img = score_font.render('Score : ' + str(SCORE), True, BLACK)
    posi = score_img.get_rect(center=(80, 60))
    screen.blit(score_img, (posi[0], posi[1] - 40))

    pygame.display.flip()
pygame.quit()
