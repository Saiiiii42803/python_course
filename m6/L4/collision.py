import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

sprite_color = "white"
background_color = "blue"

# Load and resize the background image
background = pygame.image.load(
    "m6/L1/background.jpg"
)
background = pygame.transform.scale(background, (700, 700))

running = True

colors = {"Red":(255,0,0), "green":(0,255,255)}
x = 30
y = 30
size = 30

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 20))
        self.image.fill("red")
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
    def move(self, x, y):
        pass

# Create a sprite group
all_sprites = pygame.sprite.Group()

# Create and add the sprite
player = Sprite()
target = Sprite()
player.rect.x = 20
player.image.fill("BLUE")

all_sprites.add(player, target)
won = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not won:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            player.rect.x = player.rect.x - 1
        if pressed[pygame.K_RIGHT]:
            player.rect.x = player.rect.x + 1
        if pressed[pygame.K_UP]:
            player.rect.y = player.rect.y - 1
        if pressed[pygame.K_DOWN]:
            player.rect.y = player.rect.y + 1
                
            #Keep the square inside the window
        player.rect.x = min(max(0, player.rect.x), 500 - size)
        player.rect.y = min(max(0, player.rect.y), 500 - size)
        #pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, size, size))
        if player.rect.colliderect(target.rect):
            won = True
            all_sprites.remove(target)

    screen.blit(background, (0, 0))
    
    all_sprites.draw(screen)

    font = pygame.font.SysFont("Arial", 50)

    if won == True:
        text = font.render("You win", True, "BLACK") 
        screen.blit(text, (50,60))
    pygame.display.flip()


pygame.quit()