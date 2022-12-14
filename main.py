import pygame
import os
import math
import random

pygame.init()
WIDTH, HEIGHT = 800, 500
win=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

RADIUS=20
GAP=15
letters=[]
startx=round((WIDTH - (RADIUS *2+GAP)*13)/2)
starty=400
A=65
for i in range(26):
    x= startx + GAP*2 +(RADIUS*2 + GAP)*(i%13)
    y= starty+((i//13) *(GAP+RADIUS*2))
    letters.append([x,y, chr(A+i), True])

LETTER_FONT=pygame.font.SysFont('comicsans', 32)
WORD_FONT=pygame.font.SysFont('comicsans', 32)
TITLE_GAME= pygame.font.SysFont('comicsans', 70)
images=[]
for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

hangman_status= 0
words=["PHENYLKETONURIA", "STOKE" "LEUKEMIA"]
word= random.choice(words)
guessed = []

FPS = 60
clock= pygame.time.Clock()
run = True

def draw():
    win.fill((255, 255, 255))
    text= TITLE_GAME.render("HANGMAN GAME", 1, (0, 0, 0))
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    display_world=""
    for letter in word:
        if letter in guessed:
            display_world+= letter + " "
        else:
            display_world+= "_ "
    text= WORD_FONT.render(display_world, 1 , (0, 0, 0))
    win.blit(text, (300, 200))

    for letter in letters:
        x, y, ltr, visible=letter
        if visible:
            pygame.draw.circle(win, (0, 0, 0), (x, y), RADIUS, 3)
            text= LETTER_FONT.render(ltr, 1 , (0, 0, 0))
            win.blit(text, (x-text.get_width()/2, y-text.get_height()/2))


    win.blit(images[hangman_status], (-150,0))
    pygame.display.update()
def display_message(message):
    pygame.time.delay(3000)
    win.fill((255, 255, 255))
    text= WORD_FONT.render(message, 1, (0, 0, 0))
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            m_x, m_y =pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible= letter
                if visible:
                    dis=math.sqrt((x - m_x)**2+(y-m_y)**2)
                    if dis<RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
    draw()
    won =True
    for letter in word:
        if letter not in guessed:
            won=False
            break  
    if won:
        display_message("You WIN")
        break
    if hangman_status==6:
        display_message("You LOST")
        break

pygame.quit()