import pygame
pygame.init()
screen = pygame.display.set_mode((400, 500))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()


pygame.quit()