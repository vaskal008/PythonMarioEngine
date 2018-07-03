#
# My Mario by Vasya & Papa (c) 2018
#
import pygame
import random
import constants

from sprite_helper import SpriteSheet

from player import Player

# Инициализировать Pygame
pygame.init()

screen = pygame.display.set_mode([constants.screen_width, constants.screen_height])

sprite_sheet = SpriteSheet("super-mario-sprite.png")

if sprite_sheet is not None:
    print("load sprite sheet done!")

pygame.init()
pygame.display.set_caption('Super Mario Bros By Vasya & Papa (c) 2018')


# Размеры спрайта по X и Y
SPRITE_WIDTH = 32
SPRITE_X_SIZE = SPRITE_WIDTH
SPRITE_Y_SIZE = 64

image_array = []

for i in range(0, 21):
    image_array.append(sprite_sheet.get_image(SPRITE_WIDTH * i, 0, SPRITE_X_SIZE, SPRITE_Y_SIZE))

# Создание экземпляра героя игры
mario = Player(image_array)

# Это список спрайтов. Каждый блок добавляется в этот список.
# Список управляется классом, называющимся 'Group.'
block_list = pygame.sprite.Group()

# Это список каждого спрайта. Все блоки, а также блок игрока.
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(mario)

# Быть в цикле до момента, пока пользователь не решит закрыть программу
done = False

# Используется для определения скорости обновления экрана
clock = pygame.time.Clock()

dt = 0

# -------- Основной цикл программы -----------
while done == False:

    # Очистить экран
    screen.fill(constants.white)

    for event in pygame.event.get():  # Пользователь что-то сделал
        if event.type == pygame.QUIT:  # Если пользователь нажал "закрыть"
            done = True  # Отметить, что всё готово, так чтобы программа вышла из цикла
            print("Exit")
        # Пользователь нажимает на клавишу
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
                mario.walk_left()
            if event.key == pygame.K_RIGHT:
                print("right")
                mario.walk_right()
            if event.key == pygame.K_UP:
                print("up")
                mario.walk_up()
            if event.key == pygame.K_DOWN:
                print("down")
                mario.walk_down()

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    dt = clock.tick(60)
    print(dt)