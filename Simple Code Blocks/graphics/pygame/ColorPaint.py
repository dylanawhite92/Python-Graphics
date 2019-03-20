import pygame                           # Setup
import random

# Initialize pygame modules & set window size
pygame.init()
screen = pygame.display.set_mode([1280,1024])
pygame.display.set_caption("Click and drag to draw!")

keep_going = True
PURPLE = (130, 0, 135)                  # RBG color triplets for 3 mousebuttons
ORANGE = (255, 255, 0)
BLUE = (0, 0, 255)
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
        if pygame.mouse.get_pressed()[0]:   # Boolean for left mouse button (1)
            button_color = PURPLE
        elif pygame.mouse.get_pressed()[2]: # Boolean for right mouse button (2)
            button_color = ORANGE
        else:                               # Must be button 3/mouse wheel
            button_color = BLUE
        pygame.draw.circle(screen, button_color, spot, radius)
    pygame.display.update()             # Update display

pygame.quit()
