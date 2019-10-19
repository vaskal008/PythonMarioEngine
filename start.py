#
# My Mario by Vasya & Papa (c) 2018
#
import pygame
import constants
import pyganim

from sprite_helper import SpriteSheet

# from player import Player

# Инициализировать PyGame
pygame.init()

# Объявим константы
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
JUMP = 'jump'
titleText = 'Super Mario Bros By Vasya & Papa (c) 2018'
gravity = 1.35
yVelocity = 0
onGround = False

def checkCollision(sprite1_rect, sprite2_rect):
    result = False

    if sprite1_rect.x < sprite2_rect.x + sprite2_rect.sizeX and \
       sprite1_rect.x + sprite1_rect.sizeX > sprite2_rect.x and \
       sprite1_rect.y < sprite2_rect.y + sprite2_rect.sizeY and \
       sprite1_rect.y + sprite1_rect.sizeY > sprite2_rect.y:
        result = True

    return result

# Объявим размер окна
screen = pygame.display.set_mode([constants.screen_width, constants.screen_height])

# Загружаем спрайты
sprite_sheet = SpriteSheet("super-mario-sprite.png")
blocks_sheet = SpriteSheet("blocks2.png")

if sprite_sheet is not None:
    print("load sprite sheet done!")

if blocks_sheet is not None:
    print("load blocks sheet done!")

pygame.display.set_caption(titleText)

# Размеры спрайта по X и Y
SPRITE_WIDTH = 32
SPRITE_X_SIZE = SPRITE_WIDTH
SPRITE_Y_SIZE = 64

# Создаем массив из 21 спрайта
image_array = []
for i in range(0, 22):
    image_array.append(sprite_sheet.get_image(SPRITE_WIDTH * i, 0, SPRITE_X_SIZE, SPRITE_Y_SIZE))

blocks_array = []
for i in range(0, 22):
    blocks_array.append(blocks_sheet.get_image(SPRITE_WIDTH * i, 0, SPRITE_X_SIZE, SPRITE_X_SIZE))

# Загружаем "стоячие" спрайты
right_standing = image_array[0]
left_standing = pygame.transform.flip(right_standing, True, False)

# Ground sprite
ground_sprite = blocks_array[0]

cloud_sprite = blocks_sheet.get_image(0, 2 * SPRITE_X_SIZE, 3 * SPRITE_X_SIZE, 2 * SPRITE_X_SIZE)

class cloud_sprite_rect(object):
    sizeX = 3 * SPRITE_X_SIZE
    sizeY = 2 * SPRITE_X_SIZE
    x = 0
    y = 0

    def __init__(self, SPRITE_X_SIZE, SPRITE_Y_SIZE, x, y):
        self.sizeX = 3 * SPRITE_X_SIZE
        self.sizeY = 2 * SPRITE_X_SIZE
        self.x = x
        self.y = y

class character_sprite_rect(object):
    sizeX = SPRITE_X_SIZE
    sizeY = SPRITE_Y_SIZE
    x = 0
    y = 0

    def __init__(self, SPRITE_X_SIZE, SPRITE_Y_SIZE, x, y):
        self.sizeX = SPRITE_X_SIZE
        self.sizeY = SPRITE_Y_SIZE
        self.x = x
        self.y = y

class ground_sprite_rect(object):
    sizeX = SPRITE_X_SIZE
    sizeY = SPRITE_X_SIZE
    x = 0
    y = 0

    def __init__(self, SPRITE_X_SIZE, SPRITE_Y_SIZE, x, y):
        self.sizeX = SPRITE_X_SIZE
        self.sizeY = SPRITE_X_SIZE
        self.x = x
        self.y = y

# Подготовка спрайтов для PygAnimation
animationObjects = {}
imagesAndDurations = [(image_array[3], 0.1),
                      (image_array[2], 0.1),
                      (image_array[1], 0.1)]
animationObjects['right_walk'] = pyganim.PygAnimation(imagesAndDurations)

# Переворачиваем спрайты по вертикали налево
animationObjects['left_walk'] = animationObjects['right_walk'].getCopy()
animationObjects['left_walk'].flip(True, False)
animationObjects['left_walk'].makeTransformsPermanent()

# have the animation objects managed by a conductor.
# With the conductor, we can call play() and stop() on all the animation
# objects at the same time, so that way they'll always be in sync with each
# other.
moveConductor = pyganim.PygConductor(animationObjects)

# Направление движения спрайтов по умолчанию
direction = RIGHT

# Быть в цикле до момента, пока пользователь не решит закрыть программу
done = False

# Используется для определения скорости обновления экрана
clock = pygame.time.Clock()

# Счетчик кадров
dt = 0

# Начальные координаты спрайта
x = 300
y = 200

WALKRATE = 3
JUMPRATE = 3

jump = moveUp = moveDown = moveLeft = moveRight = moveJump = False

# Подготовка текстовой инструкции
BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
instructionSurf = BASICFONT.render('Arrow keys to move. SpaceBar to jump.', True, constants.black)
instructionRect = instructionSurf.get_rect()
instructionRect.bottomleft = (10, constants.screen_height - 10)

# Основной цикл
while done == False:

    # Очистить экран
    screen.fill(constants.skyblue)

    cloudX = 100
    cloudY = 100
    screen.blit(cloud_sprite, (cloudX, cloudY))

    cloud = cloud_sprite_rect(SPRITE_X_SIZE, SPRITE_Y_SIZE, cloudX, cloudY)

    # Цикл событий
    for event in pygame.event.get():
        # Если пользователь нажал "закрыть"
        if event.type == pygame.QUIT:
            done = True  # Для выхода программы (из основного цикла)
            print("Exit")

        yVelocity += gravity

        # Пользователь нажимает на клавишу
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True  # Для выхода программы (из основного цикла)
                print("Exit")

            if event.key == pygame.K_LEFT:
                print("left")
                moveLeft = True
                moveRight = False
                direction = LEFT
            if event.key == pygame.K_RIGHT:
                print("right")
                moveLeft = False
                moveRight = True
                direction = RIGHT
            if event.key == pygame.K_UP:
                print("up")
                moveUp = True
                moveDown = False
            if event.key == pygame.K_DOWN:
                print("down")
                moveDown = True
                moveUp = False
            if event.key == pygame.K_SPACE:
                print("space")
                moveJump = True

        # Пользователь отпускает клавишу
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
            elif event.key == pygame.K_RIGHT:
                moveRight = False
            if event.key == pygame.K_UP:
                moveUp = False
            elif event.key == pygame.K_DOWN:
                moveDown = False
            # if event.key == pygame.K_SPACE:
            #     moveJump = False

    if moveUp or moveDown or moveLeft or moveRight or moveJump:
        moveConductor.play() # calling play() while the animation objects are already playing is okay; in that case play() is a no-op
        if direction == LEFT:
            animationObjects['left_walk'].blit(screen, (x, y))
        elif direction == RIGHT:
            animationObjects['right_walk'].blit(screen, (x, y))

        rate = WALKRATE

        if moveUp:
            y -= rate
        if moveDown:
            y += rate
        if moveLeft:
            x -= rate
        if moveRight:
            x += rate
        if moveJump:
            yVelocity -= JUMPRATE
            moveJump = False

        # Test collision detection
        char = character_sprite_rect(SPRITE_X_SIZE, SPRITE_Y_SIZE, x, y)
        if checkCollision(cloud, char):
            if moveUp:
                y += rate
            if moveDown:
                y -= rate
            if moveLeft:
                x += rate
            if moveRight:
                x -= rate

    else:
        # "Стоячие" спрайты
        moveConductor.stop() # останавливаем анимацию
        if direction == LEFT:
            screen.blit(left_standing, (x, y))
        elif direction == RIGHT:
            screen.blit(right_standing, (x, y))

    # Отследим чтобы спрайт не выходил за рамки экрана
    if x < 0:
        x = 0
    if x > constants.screen_width - SPRITE_X_SIZE:
        x = constants.screen_width - SPRITE_X_SIZE
    if y < 0:
        y = 0
    if y > constants.screen_height - SPRITE_Y_SIZE * 2:
        y = constants.screen_height - SPRITE_Y_SIZE * 2
        yVelocity = 0
        onGround = True
    else:
        y += yVelocity
        onGround = False

    # Ground drawing
    for i in range(0, 22):
        screen.blit(ground_sprite, (i * 32, 368))
        screen.blit(ground_sprite, (i * 32, 336))

    # Нарисуем инструкцию
    screen.blit(instructionSurf, instructionRect)

    # Обновим экран
    pygame.display.update()

    # Ограничим кадры в секунду
    dt = clock.tick(60)
