import pygame
from time import sleep

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
score = 0


pygame.display.set_caption("My Game")

clock = pygame.time.Clock()
from random import uniform as func

bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)

def drawScore():
    font = pygame.font.SysFont('Arial', 36)
    text = font.render(f"Your score: {score}", True, white)
    win.fill(black)
    win.blit(text, ((WIDTH - text.get_width()) // 2, (HEIGHT - text.get_height()) // 2))
    pygame.display.update()



def drawWindow():
    win.fill(black)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))  # up
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))  # left
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))  # right
    pygame.draw.rect(win, white, (0, HEIGHT - bound, WIDTH, bound))  # down
    pygame.display.update()
    x, y = WIDTH // 2, HEIGHT // 2
    radius = 10


run = True

while run:
    clock.tick(c2s)
if x + vx < border_l or x + vx > border_r:
     vx = -vx
#if y + vy < border_u y + vy > border_d:
     vy = -vy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and xp > bound:
xp -= vp
if keys[pygame.K_RIGHT] and xp < WIDTH - width - bound:
xp += vp


if y + vy > border_d:
    drawScore()
    pygame.time.delay(3000)
    run = False


if x + vx >= xp and x + vx <= xp + width:
        if xp <= x + vx <= xp + width:
            vy = -vy
        else:
            pass
        vx *= 1.5
        vy *= 1.5
        vy = -vy
        score += 1

x += vx
y += vy
velocity = 8
vx = velocity*func(-1, 1)
vy = velocity*func(-1, 1)

height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height

    drawWindow()
    color = (0, 255, 0)
    pygame.draw.rect(win, white, (xp, yp, width, height))
    pygame.draw.circle(win, color, (x, y), radius)

border_d = bound + radius
border_r = WIDTH - bound - radius
border_u = bound + radius
border_d = HEIGHT - bound - radius

drawScore()
sleep(10)

def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 30)
    text = ''.join([chr(int(str(el), 8)) for el in [107, 141, 155, 145, 40, 157, 166, 145, 162]])
    a = Font.render(text, 1, (255, 255, 255))
    win.blit(a, (WIDTH // 2 - 70, HEIGHT // 3))
    pygame.display.update()

pygame.quit()
