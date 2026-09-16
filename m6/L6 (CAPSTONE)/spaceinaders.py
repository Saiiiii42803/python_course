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
score = 0

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

def check_collision(enemies, bullet_x, bullet_y):

    for e in enemies:

        enemy_rect = pygame.Rect(
            e[0], e[1], 64, 64
        )

        bullet_rect = pygame.Rect(
            bullet_x, bullet_y, 32, 32
        )

        if bullet_rect.colliderect(enemy_rect):

            # Put enemy back at the top
            e[0] = random.randint(0, 736)
            e[1] = random.randint(50, 150)

            return True

    return False

def check_game_over(enemies):

    for e in enemies:

        if e[1] >= 500:
            return True

    return False


def draw_score(screen, score):

    text = font.render(
        "Score: " + str(score),
        True,
        "white"
    )

    screen.blit(text, (15, 35))



font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 64)
def draw_game_over(screen):

    text = game_over_font.render(
        "GAME OVER",
        True,
        "white"
    )

    x = (800 - text.get_width()) // 2
    y = (500 - text.get_height()) // 2

    screen.blit(text, (x, y))

bullet_x = 0
bullet_y = 380
game_over = False

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
                    bullet_x = player_x + 35
                    bullet_y = player_y + 150
                    bullet_fired = True

        # Key released
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                player_speed = 0

            if event.key == pygame.K_RIGHT:
                player_speed = 0

    if not game_over:
        player_x = move_player(player_x, player_speed)
        enemies = move_enemies(enemies)
        game_over = check_game_over(enemies)

        # Display the background, image, and text
        screen.blit(background, (0, 0))
        screen.blit(player, (player_x, 500))
        for e in enemies:
            screen.blit(enemy, (e[0], e[1]))

        # Move Bullet
        if bullet_fired:
        
            bullet_y -= 1

            # Reset bullet when it leaves screen
            if bullet_y < 0:
                bullet_fired = False

        # Check collision
        if bullet_fired:

            hit = check_collision(enemies, bullet_x, bullet_y)

            if hit:
                score += 1
                bullet_fired = False

        # Bullet
        if bullet_fired:
            screen.blit(
                bullet,
                (bullet_x, bullet_y)
            )

        draw_score(
            screen,
            score
        )
    
        # Draw Game Over
        if game_over:
    
            draw_game_over(
                screen
            )
    
    pygame.display.flip()


pygame.quit()