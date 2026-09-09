import pygame
pygame.init()
screen = pygame.display.set_mode((500, 400))

sprite_color = "white"
background_color = "blue"


running = True

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 20))
        self.image.fill("white")
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100

        self.speed_x = 1
        self.speed_y = 1

    def update(self):
        # Move the sprite
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Check if the sprite touches the left or right edge
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.speed_x = -self.speed_x

        # Check if the sprite touches the top or bottom edge
        if self.rect.top <= 0 or self.rect.bottom >= 400:
           self.speed_y = -self.speed_y

# Create a sprite group
all_sprites = pygame.sprite.Group()

# Create and add the sprite
sprite = Sprite()

all_sprites.add(sprite)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Update and draw the sprite
    all_sprites.update()

    screen.fill(background_color)
    all_sprites.draw(screen)
    
    pygame.display.flip()


pygame.quit()