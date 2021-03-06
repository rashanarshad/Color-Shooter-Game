import pygame
import random

import game
import player
import surface_manager

class PowerUp(pygame.sprite.DirtySprite):
    def __init__(self, img):
        super(PowerUp, self).__init__()
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = pygame.Rect((0, 0), (self.image.get_width(), self.image.get_height()))
        self.pos_x = self.display.get_width()
        self.pos_y = random.randint(150, 400)
        self.bonus_sound = pygame.mixer.Sound("data/sound/powerup.wav")
        self.dirty = 1

    def is_consumed(self):
        collidelist = pygame.sprite.spritecollide(self, surface_manager.surface_list, False)

        for item in collidelist:
            if type(item) is player.Player:
                return True

        return False

class BulletPU(PowerUp):
    def __init__(self):
        super(BulletPU, self).__init__("data/images/powerup.png")

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)

        if self.is_consumed():
            self.add_bonus()
            surface_manager.remove(self)

        self.pos_x -= 12

        self.rect.topleft = (self.pos_x, self.pos_y)
        self.dirty = 1

    def add_bonus(self):
        self.bonus_sound.play()
        game.Game.player.bullets += 50
class PowerUp2(pygame.sprite.DirtySprite):
    def __init__(self, img):
        super(PowerUp2, self).__init__()
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = pygame.Rect((0, 0), (self.image.get_width(), self.image.get_height()))
        self.pos_x = self.display.get_width()
        self.pos_y = random.randint(150, 400)
        self.bonus_sound = pygame.mixer.Sound("data/sound/powerup.wav")
        self.dirty = 1

    def is_consumed(self):
        collidelist = pygame.sprite.spritecollide(self, surface_manager.surface_list, False)

        for item in collidelist:
            if type(item) is player.Player:
                return True

        return False

class BulletPU2(PowerUp2):
    def __init__(self):
        super(BulletPU2, self).__init__("data/images/powerup_2.png")

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)

        if self.is_consumed():
            self.add_bonus()
            surface_manager.remove(self)

        self.pos_x -= 12

        self.rect.topleft = (self.pos_x, self.pos_y)
        self.dirty = 1

    def add_bonus(self):
        self.bonus_sound.play()
        game.Game.player.bullets2 += 3