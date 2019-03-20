import pygame                           # Setup

pygame.init()

screen = pygame.display.set_mode([1280,1024])
pygame.display.set_caption("Click and drag to draw!")

keep_going = True
PURPLE = (130,0,135)                    # RGB color triplet for PURPLE
radius = 15                             # 'Brush' width
mousedown = False                       # Boolean signal that button is pressed

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
        pygame.draw.circle(screen, PURPLE, spot, radius)
    pygame.display.update()             # Update display

pygame.quit()
