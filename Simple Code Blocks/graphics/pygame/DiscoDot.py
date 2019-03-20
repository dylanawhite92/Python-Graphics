import pygame
import random

# Initialize imported pygame modules & set canvas size
pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going = True
PURPLE = (130,0,130)    # RGB color triplet for PURPLE
radius = random.randint(10,200)

# With every move of the mouse, change the color of the drawn dot
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pygame.draw.circle(screen, color, (400,300), radius)
        pygame.display.update()

pygame.quit()
