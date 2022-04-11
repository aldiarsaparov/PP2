import pygame 
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

font = pygame.font.SysFont("Arial", 40)

# creating food
class Food:
    def __init__(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
    
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, cell, cell))
    
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
        self.body = [[80, 80], [1000, 1000], [1040, 1040], [1080, 1080], [1120, 1120]]
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

        if self.body[0][0]> WIDTH:
            self.body[0][0] = 0
        
        if self.body[0][1] > HEIGHT:
            self.body[0][1] = 0

        if self.body[0][0] < 0:
            self.body[0][0] = WIDTH
        
        if self.body[0][1] < 0:
            self.body[0][1] = HEIGHT

        self.body[0][0] % WIDTH
        self.body[0][1] %= HEIGHT
    
    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color, (block[0], block[1], cell, cell))

    # eating an apple 
    def collide_food(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            self.body.append([1000, 1000])
        
    # death
    def collide_self(self):
        global finished, lose
        if self.body[0] in self.body[1:]:
            lose = True
    
    # creating new apple
    def check_food(self, f:Food):
        if [f.x, f.y] in self.body:
            f.redraw()
            global SCORE
            SCORE += 1

s = Snake()
f = Food()

SCORE = 0
lose = False
level = 0

while not finished:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
        if SCORE >= 3:
            FPS = 15
            level = 1

    screen.fill(WHITE)

    walls_coor = open(f"wall{level}.txt", "r").readlines()

    walls = []

    for i, line in enumerate(walls_coor):
        for j, each in enumerate(line):
            if each == "#":
                walls.append(Wall(j * cell, i * cell))
    
    while lose:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = not finished
                    lose = not lose
            go_font = pygame.font.SysFont("Arial", 40)
            go_img = go_font.render("You lost!", True, BLACK)
            screen.blit(go_img, go_img.get_rect(center = (WIDTH // 2, HEIGHT // 2)))
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
        
    score_font = pygame.font.SysFont("Arial", 40)
    score_img = score_font.render('Score : ' + str(SCORE), True, BLACK)
    posi =  score_img.get_rect(center = (200, 60))
    screen.blit(score_img, (posi[0], posi[1] - 40))

    pygame.display.flip()
pygame.quit()


        