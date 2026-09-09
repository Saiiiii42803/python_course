import pygame
pygame.init()
screen = pygame.display.set_mode((500, 400))

# Create the sprite
x = 100
y = 100
width = 30
height = 20

speed_x = 0.5
speed_y = 0.5

sprite_color = "white"
background_color = "blue"


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the sprite
    x += speed_x
    y += speed_y

    # Check if the sprite touches the left or right edge
    if x <= 0 or x + width >= 500:
        speed_x = -speed_x

    # Check if the sprite touches the top or bottom edge
    if y <= 0 or y + height >= 400:
        speed_y = -speed_y


    screen.fill(background_color)
    pygame.draw.rect(screen, sprite_color, pygame.Rect(x, y, width, height))
    
    pygame.display.flip()


pygame.quit()