import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

running = True
colors = {"Red":(255,0,0), "green":(0,255,255)}
x = 30
y = 30
size = 30
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x = x - 0.1
    if pressed[pygame.K_RIGHT]:
        x = x + 0.1
    if pressed[pygame.K_UP]:
        y = y - 0.1
    if pressed[pygame.K_DOWN]:
        y = y + 0.1

    # Keep the square inside the window
    x = min(max(0, x), 500 - size)
    y = min(max(0, y), 500 - size)
    screen.fill("black")
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, size, size))

    pygame.display.flip()


pygame.quit()