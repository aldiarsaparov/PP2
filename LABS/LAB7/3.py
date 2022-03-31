import pygame as pg

pg.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("BALL")

finished = False

x = WIDTH // 2 + 100
y = HEIGHT // 2 - 100
radius = 25

clock = pg.time.Clock()

while not finished:
    clock.tick(50) 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    keys = pg.key.get_pressed()
    if keys[pg.K_UP] and y - radius > 0:
        y -= 20
    if keys[pg.K_DOWN] and y + radius <= HEIGHT:
        y += 20
    if keys[pg.K_RIGHT] and x + radius <= WIDTH:
          x += 20
    if  keys[pg.K_LEFT] and x - radius > 0:
          x -= 20

    screen.fill(WHITE)

    pg.draw.circle(screen, RED, (x, y), radius)
    pg.display.flip()
    
pg.quit()