import pygame                           # Setup
import random

pygame.init()

screen = pygame.display.set_mode([1280,1024])
pygame.display.set_caption("Click and drag to draw!")
keep_going = True
PURPLE = (130, 0, 135)
radius = 15                             # 'Brush' width
mousedown = False                       # Boolean signal that button isn't pressed

while keep_going:                       # Game loop
    for event in pygame.event.get():    # Handling events
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if mousedown:                       # Draw/update graphics
        spot = pygame.mouse.get_pos()
        randcolor = (random.randrange(0,255), random.randrange(0,255),
                     random.randrange(0,255))
        pygame.draw.circle(screen, randcolor, spot, radius)
    pygame.display.update()             # Update display

pygame.quit()
