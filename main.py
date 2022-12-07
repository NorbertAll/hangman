import pygame
import os

pygame.init()
WIDTH, HEIGHT = 800, 500
win=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

images=[]
for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".jpg")
    images.append(image)

hangman_status= 0

FPS = 60
clock= pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    win.fill((255, 255, 255))
    win.blit(images[hangman_status], (0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            print(position)
pygame.quit()