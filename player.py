import pygame
import constants

# Он наследуется от класса "Sprite" из Pygame
class Player(pygame.sprite.Sprite):

    walk_animation = [1, 2, 3]
    jump_animation = [4, 5, 6]
    swim_animation = [7, 8, 9, 10, 11, 12, 13, 14]

    WALKING_SPEED = 20

    # Конструктор. Ему передаётся цвет блока,
    # а также его ширина и высота
    def __init__(self, sprite_image_array):
        # Вызвать конструктор родительского класса (Sprite)
        super().__init__()

        self.image_array = sprite_image_array

        self.image = sprite_image_array[self.walk_animation[2]]
        self.rect = self.image.get_rect()

    def walk_up(self):
        if (self.rect.y - self.WALKING_SPEED) >= 0:
            self.rect.y -= self.WALKING_SPEED


    def walk_down(self):
        if (self.rect.y + self.WALKING_SPEED) <= constants.screen_height:
            self.rect.y += self.WALKING_SPEED

    def walk_left(self):
        if (self.rect.x - self.WALKING_SPEED) >= 0:
            self.rect.x -= self.WALKING_SPEED

    def walk_right(self):
        if (self.rect.x + self.WALKING_SPEED) <= constants.screen_width:
            self.rect.x += self.WALKING_SPEED
