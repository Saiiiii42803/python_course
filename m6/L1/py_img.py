import pygame
pygame.init()
screen = pygame.display.set_mode((700, 700))


# Load and resize the background image
background = pygame.image.load(
    "m6/L1/background.jpg"
)
background = pygame.transform.scale(background, (700, 700))

# Load and resize the penguin image
penguin = pygame.image.load(
    "m6/L1/penguin.png"
)

penguin = pygame.transform.scale(penguin, (200, 200))



running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the background, image, and text
    screen.blit(background, (0, 0))
    screen.blit(penguin, (150, 100))
    
    pygame.display.flip()


pygame.quit()