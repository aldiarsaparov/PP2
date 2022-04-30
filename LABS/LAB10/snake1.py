from random import randint, randrange
from config import data
import psycopg2
import pygame

config = psycopg2.connect(**data)

current = config.cursor()

print("Enter your name")
username = input()

sql = '''
    SELECT * FROM users WHERE user_name = %s;
'''
current.execute(sql, [username])
data = current.fetchone()

if data == None:
    sql = '''
        INSERT INTO users VALUES(%s, 0, 0);
    '''
    current.execute(sql, [username])
    config.commit()

pygame.init()

WIDTH, HEIGHT = 800, 640
FPS = 7
cell = 40

score = 0

font = pygame.font.SysFont("Proxima Nova", 40, True)
font_pause=pygame.font.SysFont("Proxima Nova", 50, True)
font_medium = pygame.font.SysFont("Voltec", 40)
game_over = font_medium.render("Game Over", True, (250,250,250))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221, 160, 221)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

finished = False
lose = False

clock = pygame.time.Clock()
def paused(username,level,score):
    current.execute(sql, [score, level, username])

class Food:
    def __init__(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, cell, cell))

    def redraw(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)


class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, cell, cell))


class Snake:
    def __init__(self):
        self.speed = cell
        self.score = 0
        self.body = [[80, 80], [1000, 1000], [
            1040, 1040], [1080, 1080], [1120, 1120]]
        self.dx = self.speed
        self.dy = 0
        self.destination = ''
        self.color = GREEN

    def move(self, events):
        global pause
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.destination != 'right':
                    self.dx = -self.speed
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_d and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_w and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                if event.key == pygame.K_s and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'
                if event.key == pygame.K_SPACE:
                    pause=True
                if event.key==pygame.K_p:
                    pause=False 

        # for i in range(len(self.body) - 1, 0, -1):
        #     self.body[i][0] = self.body[i - 1][0]
        #     self.body[i][1] = self.body[i - 1][1]

        # self.body[0][0] += self.dx
        # self.body[0][1] += self.dy

        # self.body[0][0] %= WIDTH
        # self.body[0][1] %= HEIGHT
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

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color,
                             (block[0], block[1], cell, cell))

    def collide_food(self, f: Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            self.score += 1
            self.body.append([1000, 1000])

    def collide_self(self):
        global finished, lose
        if self.body[0] in self.body[1:]:
            finished = True
            lose = True

    def check_food(self, f: Food):
        if [f.x, f.y] in self.body:
            f.redraw()
            global score
            score += randint(1, 3) # random weight


s = Snake()
f = Food()
score = 0
highscore = 0
level = 0
pause = False

while not finished:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause = True

    while pause:
        render_end = font_pause.render("PAUSE", True, pygame.Color('orange'))
        screen.blit(render_end, (335, 300))
        pygame.display.flip()
        
        sql = '''
            UPDATE users SET score = %s, level = %s WHERE user_name = %s;
        '''
        current.execute(sql, [score, level, username]) 
        config.commit()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            pause = False 

    walls_coor = open(f"wall{level}.txt", "r").readlines()

    walls = []

    # creating walls
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
            go_img = go_font.render("Game Over!", True, BLACK)
            screen.blit(go_img, go_img.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            pygame.display.flip()

    screen.fill(WHITE)
    if s.score == 3:
        level = 1
        FPS = 9
    if s.score == 5:
        level = 2
        FPS = 11
    if s.score == 7:
        level = 3
        FPS = 13

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

    text = font.render(f"Score:{s.score}", True, BLACK)
    text2 = font.render(f"Level: {level}", True, BLACK)
    screen.blit(text, (0, 0))
    screen.blit(text2, (150, 0))
    pygame.display.flip()
    score = s.score

pygame.quit()
sql = '''
    UPDATE users SET score = %s, level = %s WHERE user_name = %s;
'''

current.execute(sql, [score, level, username])
config.commit()
current.close()
config.close()
