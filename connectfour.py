import pygame
import sys
from pygame.locals import *


def win(Matrix):
    for a in range(len(Matrix)):
        for b in range(len(Matrix[0])):
            if a < 3 and b < 4:
                if Matrix[a][b] == Matrix[a + 1][b + 1] == Matrix[a + 2][b + 2] == Matrix[a + 3][b + 3] != 0:
                    return Matrix[a][b]
            if a > 2 and b < 4:
                if Matrix[a][b] == Matrix[a - 1][b + 1] == Matrix[a - 2][b + 2] == Matrix[a - 3][b + 3] != 0:
                    return Matrix[a][b]
            if a < 3:
                if Matrix[a][b] == Matrix[a + 1][b] == Matrix[a + 2][b] == Matrix[a + 3][b] != 0:
                    return Matrix[a][b]
            if b < 4:
                if Matrix[a][b] == Matrix[a][b + 1] == Matrix[a][b + 2] == Matrix[a][b + 3] != 0:
                    return Matrix[a][b]
    return 0


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ConnectFour")
clock = pygame.time.Clock()

Matrix = [[0 for x in range(7)] for y in range(6)]
pos = 0
now = 1
winner = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                Matrix = [[0 for x in range(7)] for y in range(6)]
                pos = 0
                now = 1
                winner = 0
            if event.key == K_LEFT:
                if pos > 0:
                    pos -= 1
            if event.key == K_RIGHT:
                if pos < 6:
                    pos += 1
            if event.key == K_DOWN:
                for c in range(len(Matrix)-1, -1, -1):
                    if Matrix[c][pos] == 0:
                        Matrix[c][pos] = now
                        if now == 1:
                            now = 2
                        else:
                            now = 1
                        break
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 150, 255), (0, 0, 700, 600))

    pygame.draw.rect(screen, (0, 255, 0), (pos*100, 0, 100, 50))

    myfont = pygame.font.SysFont("monospaced", 18)

    label = myfont.render("Player:", 10, (0, 0, 0))
    screen.blit(label, (700, 0))

    if now == 1:
        pygame.draw.circle(screen, (204, 0, 0), (750, 100), 48)
    else:
        pygame.draw.circle(screen, (255, 255, 0), (750, 100), 48)

    for f in range(len(Matrix)):
        for g in range(len(Matrix[0])):
            if Matrix[f][g] == 1:
                pygame.draw.circle(screen, (204, 0, 0), (g*100+50, f*100+50), 48)
            elif Matrix[f][g] == 2:
                pygame.draw.circle(screen, (255, 255, 0), (g*100+50, f*100+50), 48)
            else:
                pygame.draw.circle(screen, (255, 255, 255), (g*100+50, f*100+50), 48)
    winner = win(Matrix)

    if winner != 0:
        if winner == 1:
            myfon = pygame.font.SysFont("monospaced", 100)

            lab = myfon.render("Red Wins", 10, (0, 0, 0))
            screen.blit(lab, (100, 200))
            pygame.display.update()
        elif winner == 2:
            myfon = pygame.font.SysFont("monospaced", 100)

            lab = myfon.render("Yellow Wins", 10, (0, 0, 0))
            screen.blit(lab, (100, 200))
            pygame.display.update()

        myfont = pygame.font.SysFont("monospaced", 40)

        lab = myfont.render("Space to Reset", 10, (0, 0, 0))
        screen.blit(lab, (150, 300))
        pygame.display.update()

    while winner != 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    Matrix = [[0 for x in range(7)] for y in range(6)]
                    pos = 0
                    now = 1
                    winner = 0

    pygame.display.update()

