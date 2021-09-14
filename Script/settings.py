import sys
import json
import pygame
from pygame.locals import *
from render import renderImage

with open('Data/settings.json', 'r') as settingsFile:
    settings = json.load(settingsFile)
    for entry in settings:
        print(entry)

resoultion = 'test'

pygame.init()
pygame.display.set_caption("Kriag's Krazy Car Game")
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode(resoultion, 0, 32)
font = pygame.font.Font("Components\pressStart.ttf", 45)


def controls():
    running = True
    while running:
        screen.fill((243, 243, 243))

        mx, my = pygame.mouse.get_pos()

        banner = pygame.Rect(0, 0, 1280, 120)

        pygame.display.set_caption("Kriag's Krazy Car Game - Controls")
        pygame.draw.rect(screen, (191, 10, 48), banner)
        text("Kriag's Krazy Controls", pygame.font.Font("Components\pressStart.ttf", 45),
             (0, 0, 0), screen, 70, 25)

        x = -50
        y = 100

        imageControls = renderImage("controls.jpg")

        def controlsImage(x, y):
            screen.blit(imageControls, (x, y))

        controlsImage(x, y)

        buttonBack = pygame.Rect(50, 620, 225, 60)

        if buttonBack.collidepoint((mx, my)):
            if click:
                mainMenu()

        pygame.draw.rect(screen, (191, 10, 48), buttonBack)
        text("BACK", pygame.font.Font("Components\pressStart.ttf", 35),
             (0, 0, 0), screen, 65, 635)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(75)
