import pygame     # Setup

pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going = True
pic = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()  # Timer for animation
speedx = 5                    # Horizontal movement in pixels per frame
speedy = 5                    # Vertical movement in pixels per frame

while keep_going:            # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    picx += speedx
    picy += speedy

    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0 or picy + pic.get_height() >= 600:
        speedy = -speedy

    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    pygame.display.update()
    timer.tick(90)           # Limit to 90 frames per second

pygame.quit()                # Exit
