import random

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

FPS = pygame.time.Clock()

screen = width, heigth = 920, 800

BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255,255,0
WHITE = 255, 255, 255

main_surface = pygame.display.set_mode(screen)
bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen)

ball = pygame.image.load('player.png').convert_alpha()
ball_rect = ball.get_rect()
ball_coord = 1


font = pygame.font.SysFont('Verdana', 20)

counter = 0 

def creat_enemy ():
    enemy = pygame.Surface((20, 20))
    enemy.fill(RED)
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(width, random.randint(0, heigth), *enemy.get_size())
    enemy_speed = random.randint(1, 4)
    return [enemy, enemy_rect, enemy_speed]

def creat_bonus():
    bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus_rect = pygame.Rect(random.randint(0, width - 30), 0, *bonus.get_size())
    bonus_speed = random.randint(1, 2)
    return [bonus, bonus_rect, bonus_speed]

CREATE_ENEMY = pygame.USEREVENT 
pygame.time.set_timer(CREATE_ENEMY, 2500)
CREATE_BONUS = pygame.USEREVENT 
pygame.time.set_timer(CREATE_BONUS, 1000)

enemies = []
bonuses = []



print("GGHHGFFGFGFHG:", 4, 78, 12, sep="&", end="\n")
print('second "line')
print(10 + 10)
print(10 - 5)
print(7 ** 7)
print(10 // 4 )
print(min(67, 100, -98, -3))
print(max(67, 100, -98, -3))
print(abs(-98))


is_working = True

while is_working:

    FPS.tick(260)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
        if event.type == CREATE_ENEMY:
            enemies.append(creat_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(creat_bonus())

    pressed_keys = pygame.key.get_pressed()

    #main_surface.fill(BLACK)
    main_surface.blit(bg, (0, 0))
    main_surface.blit(ball, ball_rect)
    main_surface.blit(font.render(("Score:" + str(counter)), True, YELLOW), (width - 110, 0)) 
    # окончание игры
    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

        if ball_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom <= 0:
           bonuses.pop(bonuses.index(bonus))
    # cчет
        if ball_rect.colliderect(bonus[1]):
           bonuses.pop(bonuses.index(bonus))
           counter += 1

    # движение мяча    
    if pressed_keys[K_DOWN] and not ball_rect.bottom >= heigth:
        ball_rect = ball_rect.move(0, ball_coord)

    if pressed_keys[K_UP] and not ball_rect.top <= 0:
        ball_rect = ball_rect.move(0, -ball_coord)

    if pressed_keys[K_RIGHT] and not ball_rect.right >= width:
        ball_rect = ball_rect.move(ball_coord, 0)

    if pressed_keys[K_LEFT] and not ball_rect.left <= 0:
        ball_rect = ball_rect.move(-ball_coord, 0) 

   
    
    pygame.display.flip()

