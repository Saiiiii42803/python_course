import pygame
import random

pygame.init()
screen = pygame.display.set_mode((850, 850))

# Load and resize the background image
background = pygame.image.load(
    "m6/L6 (CAPSTONE)/background.jpg"
)
background = pygame.transform.scale(background, (850, 850))

# Load and resize the player image
player = pygame.image.load(
    "m6/L6 (CAPSTONE)/player.png"
)

# Load and resize the player image
enemy = pygame.image.load(
    "m6/L6 (CAPSTONE)/enemy.png"
)

bullet = pygame.image.load(
    "m6/L6 (CAPSTONE)/bullet.png"
)

player = pygame.transform.scale(player, (100, 100))


player_x = 370
player_y = 380
player_speed = 0


# Move player
def move_player(x, speed):
    x += speed

    if x < 0:
        x = 0

    if x > 736:
        x = 736

    return x


enemies = []

for i in range(6):

    x = random.randint(0, 736)
    y = random.randint(50, 150)

    # [x position, y position, speed]
    enemies.append([x, y, 0.5])

def move_enemies(enemies):

    for e in enemies:

        e[0] += e[2]

        # Change direction at the edge
        if e[0] <= 0 or e[0] >= 736:
            e[2] = -e[2]
            e[1] += 40

    return enemies

running = True
bullet_fired = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed = -1
            if event.key == pygame.K_RIGHT:
                player_speed = 1
            if event.key == pygame.K_SPACE:
                if not bullet_fired:
                    bullet_x = player_x
                    bullet_y = player_y
                    bullet_fired = True

        # Key released
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                player_speed = 0

            if event.key == pygame.K_RIGHT:
                player_speed = 0

    player_x = move_player(player_x, player_speed)
    enemies = move_enemies(enemies)
    # Display the background, image, and text
    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, 500))
    for e in enemies:
        screen.blit(enemy, (e[0], e[1]))

    
    
    pygame.display.flip()


pygame.quit()