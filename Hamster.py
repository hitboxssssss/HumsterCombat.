import pygame
import random
from time import sleep

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.font.init()
font1 = pygame.font.Font(None, 80)
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
BLACK = (0, 0, 0)

def draw_button(screen, text, position, size):
    font = pygame.font.Font(None, 50)
    button_text = font.render(text, True, (255, 255, 255))
    button_rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, (0, 0, 255), button_rect)
    screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2,
                              button_rect.y + (button_rect.height - button_text.get_height()) // 2))
    return button_rect

def reset_game():
    global player, block1, block2, running
    player = pygame.Rect(screen.get_width() / 2 - 25, 600, 50, 50)
    block1_width = random.randint(50, 1210)
    block1_height = 50
    block1 = pygame.Rect(0, 0, block1_width, block1_height)
    block2 = pygame.Rect(70 + block1.width, 0, 1280 - 70 - block1_width, block1_height)
    running = True

reset_game()

while True:
    while running:
        if block1.y >= 720:
            block1.y = 0
            block2.y = 0
            block1.width = random.randint(50, 1210)
            block2.x = block1.width + 70
            block2.width = 1280 - 70 - block1.width

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player.x += 8
        if keys[pygame.K_LEFT]:
            player.x -= 8

        screen.fill("lime")
        
        block1.y += 3
        block2.y += 3

        pygame.draw.rect(screen, BLACK, player)
        pygame.draw.rect(screen, BLACK, block1)
        pygame.draw.rect(screen, BLACK, block2)

        if pygame.Rect.colliderect(player, block1) or pygame.Rect.colliderect(player, block2):
            screen.blit(lose, (500, 300))
            button_rect = draw_button(screen, "Играть снова", (540, 400), (200, 80))
            pygame.display.flip()
            running = False

        pygame.display.flip()
        clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                reset_game()

    screen.fill("lime")
    screen.blit(lose, (500, 300))
    button_rect = draw_button(screen, "Играть снова", (540, 400), (200, 80))
    pygame.display.flip()
