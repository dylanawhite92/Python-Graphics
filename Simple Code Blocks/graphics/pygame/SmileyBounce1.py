import pygame     # Setup

pygame.init()
screen = pygame.display.set_mode([600,600])

keep_going = True
pic = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()  # Timer for animation
speed = 5                    # Movement in pixels per frame

while keep_going:            # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    picx += speed            # Move the picture by
    picy += speed            # increments of 1 pixel

    if picx <= 0 or picx + pic.get_width() >= 600:
        speed = -speed

    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    pygame.display.update()
    timer.tick(90)           # Limit to 90 frames per second

pygame.quit()                # Exit
