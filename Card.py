import pygame
import time
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Happy Birthday!")
Page = 1

image1 = pygame.image.load("1.png")
image2 = pygame.image.load("2.png")
image3 = pygame.image.load("3.png")

image1 = pygame.transform.scale(image1,(700,500))
image2 = pygame.transform.scale(image2,(700,500))
image3 = pygame.transform.scale(image3,(700,500))

while (True):

    if Page == 1 :
        screen.fill((255,255,255))
        screen.blit(image1,(0,0))
        pygame.display.update()
    elif Page == 2:
        screen.fill((255,255,255))
        screen.blit(image2,(0,0))
        pygame.display.update()
    else :
        screen.fill((255,255,255))
        screen.blit(image3,(0,0))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN :
            if Page == 1 :
                Page = 2
            elif Page == 2:
                Page = 3
            else :
                Page = 1
            

        
