import pygame
import time

pygame.init()
screen=pygame.display.set_mode((1500,1000))
done=False
x = 80
y = 70
z = 1400
c = 900
ts1 = time.time()
ts2 = time.time()
tol1 = 0
tol2 = 0
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    screen.fill((0, 0, 0))
    w1 = pygame.draw.rect(screen, (0, 180, 10), pygame.Rect(200, 0, 50, 850))
    w2 = pygame.draw.rect(screen, (0, 180, 10), pygame.Rect(1200, 160, 50, 1000))
    fl = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(700, 450, 65, 65))
    w3 = pygame.draw.rect(screen, (0, 180, 10), pygame.Rect(400, 280, 50, 1000))
    w4 = pygame.draw.rect(screen, (0, 180, 10), pygame.Rect(1200, 280, 50, 1000))
    w5 = pygame.draw.rect(screen, (0, 180, 10), pygame.Rect(0, -20, 250, 30))
    w6 = pygame.draw.rect(screen, (0, 180, 10), pygame.Rect(1000, -20, 500, 30))
    w7 = pygame.draw.rect(screen, (0, 180, 10), pygame.Rect(0, 990, 450, 30))
    w8 = pygame.draw.rect(screen, (0, 180, 10), pygame.Rect(1200, 990, 750, 30))
    w9 = pygame.draw.rect(screen, (0, 180, 10), pygame.Rect(980, 0, 50, 700))
    I = pygame.image.load("dde-removebg-preview.png")
    pl1 = I.get_rect()
    pl1.center = (x, y)
    screen.blit(I, pl1)
    I = pygame.image.load("It_Was_Me__Dio_-removebg-preview.png")
    pl2 = I.get_rect()
    pl2.center = (z, c)
    screen.blit(I, pl2)
    if pl1.colliderect(fl):
        x = 80
        y = 70
    if pl2.colliderect(fl):
        z = 1400
        c = 900
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -= 3
    if pressed[pygame.K_s]: y += 3
    if pressed[pygame.K_a]: x -= 3
    if pressed[pygame.K_d]: x += 3
    if pressed[pygame.K_LEFT]: z -= 3
    if pressed[pygame.K_RIGHT]: z += 3
    if pressed[pygame.K_UP]: c -= 3
    if pressed[pygame.K_DOWN]: c += 3

    if pl1.colliderect(w1) or pl1.colliderect(w2) or pl1.colliderect(w3) or pl1.colliderect(w4) or pl1.colliderect(
            w5) or pl1.colliderect(w6) or pl1.colliderect(w7) or pl1.colliderect(w8) or pl1.colliderect(w9):
        if pressed[pygame.K_w]: y += 50
        if pressed[pygame.K_s]: y -= 50
        if pressed[pygame.K_a]: x += 50
        if pressed[pygame.K_d]: x -= 50
    if pl2.colliderect(w1) or pl2.colliderect(w2) or pl2.colliderect(w3) or pl2.colliderect(w4) or pl2.colliderect(
            w5) or pl2.colliderect(w6) or pl2.colliderect(w7) or pl2.colliderect(w8) or pl2.colliderect(w9):
        if pressed[pygame.K_UP]: c += 50
        if pressed[pygame.K_DOWN]: c -= 50
        if pressed[pygame.K_LEFT]: z += 50
        if pressed[pygame.K_RIGHT]: z -= 50
    if pl2.colliderect(fl):
        x = 80
        y = 70
        te2 = time.time()
        tol2 = round(te2 - ts2, 2)
        ts2 = time.time()
    Font2 = pygame.font.SysFont("comicsansms", 20, True, True)
    Time2 = Font2.render("Time for blue:" + str(tol2), True, (0, 0, 250))
    screen.blit(Time2, (800, 550))
    if pl1.colliderect(fl):
        z = 1400
        c = 900
        te1 = time.time()
        tol1 = round(te1 - ts1, 2)
        ts1 = time.time()
    Font1 = pygame.font.SysFont("comicsansms", 20, True, True)
    Time1 = Font1.render("Time for yellow:" + str(tol1), True, (200, 200, 0))
    screen.blit(Time1, (460, 400))
    Font = pygame.font.SysFont("comicsansms", 170, True, True)
    Title = Font.render("Maze racing", True, (0, 10, 150))
    screen.blit(Title, (250, -50))
    pygame.display.flip()
    clock.tick(60)






