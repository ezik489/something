import sys
import pygame
import barvy
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
fps = 60

forward = pygame.K_a
backwards = pygame.K_d
left = pygame.K_w
right = pygame.K_s

pozice = [50, 50]
rychlost = [0, 0]

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            #PRESSED
            if event.key == forward:
                rychlost[1] = -5
            if event.key == backwards:
                rychlost[1] = 5
            if event.key == left:
                rychlost[0] = -5
            if event.key == right:
                rychlost[0] = 5

        if event.type == pygame.KEYUP:
            #LET GO
            if event.key == forward:
                rychlost[1] = 0
            if event.key == backwards:
                rychlost[1] = 0
            if event.key == left:
                rychlost[0] = 0
            if event.key == right:
                rychlost[0] = 0

    screen.fill(barvy.WHITE)

    pozice[0] += rychlost[1]
    pozice[1] += rychlost[0]

    pygame.draw.rect(
        screen, barvy.RED, (pozice[0], pozice[1], 60, 30))

    pygame.display.update()
    clock.tick(fps)