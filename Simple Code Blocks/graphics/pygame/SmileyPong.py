# SmileyPong.py, Version 1.0
import pygame
pygame.init()

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Whack! That! Face!")

keep_going = True
pic = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)                 # Paddle color
timer = pygame.time.Clock()             # Timer for animation
speedx = 5                              # Horizontal movement in pixels per frame
speedy = 5                              # Vertical movement in pixels per frame
paddlew = 200                           # Paddle dimensions
paddleh = 25
paddlex = 300
paddley = 550
points = 0
lives = 5

while keep_going:                       # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    picx += speedx
    picy += speedy

    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0:
        speedy = -speedy
        
    if picy >= 500:
        lives -= 1
        speedy = -speedy

    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    paddlex = pygame.mouse.get_pos()[0]
    paddlex -= paddlew/2
    pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))
    pygame.display.update()
    timer.tick(90)              # Limit to 90 frames per second

pygame.quit()                           # Exit
