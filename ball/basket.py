# -*- coding: utf-8 -*-
# @Time    : 19-7-17 下午2:09
# @Author  : shenyingying
# @Email   : shen222ying@163.com
# @File    : basket.py
# @Software: PyCharm

import pygame
import random


class Basket(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.default_image_str = ['source/b.png']
        self.dead_image_str = []
        self.dead_image = []
        self.default_image = []
        self.dead_music_str = ['']
        self.speed = 50
        self.life = 5
        self.score = 0
        self.bg_size = bg_size
        for each in self.dead_image_str:
            image = pygame.image.load(each)
            self.dead_image.append(image)
        for each in self.default_image_str:
            image = pygame.image.load(each)
            self.default_image.append(image)
        self.rect = self.default_image[0].get_rect()

        # 初始化位置
        self.rect.x, self.rect.y = bg_size[0] // 2, bg_size[1] - self.rect.height

        self.mask = pygame.mask.from_surface(self.default_image[0])
        self.Full = False

    # 上下左右四个方向
    def move(self, side):
        self.rect = self.rect.move([side[0] * self.speed, side[1] * self.speed])
        if self.rect.right > self.bg_size[0]:
            self.rect.right = self.bg_size[0]
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > self.bg_size[1]:
            self.rect.bottom = self.bg_size[1]
        if self.rect.top < 0:
            self.rect.top = 0

    def dead(self):
        self.dead_sound = pygame.mixer.Sound(self.dead_music_str)
        self.dead_sound.play()


class Protection_cover(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.bg_size = bg_size
        self.image = pygame.image.load('/home/sy/paper/childCode/TutorABC -python初级课件/code/maze/source/user.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, centerX, centerY):
        self.rect.centerX, self.rect.centerY = centerX, centerY
