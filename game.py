import pygame
import sys

# init
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Batman's First Game")
clock = pygame.time.Clock()

# player
player_size = 50
player_color = (255, 255, 0)  # green 
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # background + player
    screen.fill((30, 30, 30))  # dark background
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    pygame.display.flip()
    clock.tick(60) 