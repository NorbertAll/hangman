import pygame
import os

pygame.init()
WIDTH, HEIGHT = 800, 500
win=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

FPS = 60
clock= pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            print(position)
pygame.quit()