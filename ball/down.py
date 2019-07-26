# -*- coding: utf-8 -*-
# @Time    : 19-7-17 下午1:13
# @Author  : shenyingying
# @Email   : shen222ying@163.com
# @File    : down.py
# @Software: PyCharm

import pygame
import random


class Down(pygame.sprite.Sprite):
    def __init__(self, image_name_str, dead_music_str, bg_size=(800, 600), speed=1):
        # 调用父类初始化方法
        super().__init__()
        self.default_image = []
        self.image_name_str = image_name_str
        self.dead_name_image = []
        self.dead_music_str = dead_music_str
        self.bg_size = bg_size
        self.speed = speed
        self.disappear = False

    def init_image(self):
        for each in self.image_name_str:
            image = pygame.image.load(each)
            self.default_image.append(image)
        # image 的 get_rect() 方法，可以返回 pygame.Rect(0, 0, 图像宽, 图像高) 的对象
        self.rect = self.default_image[0].get_rect()
        self.mask = pygame.mask.from_surface(self.default_image[0])

    def init_pos(self, x, y):
        if self.rect.w > x:
            self.rect.left, self.rect.top = self.rect.w, y - self.rect.height
        if x > self.bg_size[0] - self.rect.w:
            self.rect.left, self.rect.top = x - self.rect.w, y - self.rect.height
        else:
            self.rect.left, self.rect.top = x, y - self.rect.height

    def move(self):
        self.rect.y += self.speed
        if self.bg_size[1] + self.rect.height < self.rect.bottom:
            self.disappear = True

    def inBasket(self):
        self.dead_sound = pygame.mixer.Sound(self.dead_music_str)
        self.dead_sound.play()


class FireBall(Down):
    def __init__(self):
        super().__init__(image_name_str=['source/fb.png'], dead_music_str='music/fb.wav')
        self.downType = 'fireBall'
        self.speed = random.randint(1, 3)
        self.score = -10


class Diamond(Down):
    def __init__(self):
        super().__init__(image_name_str=['source/d.png'], dead_music_str='music/diamond.wav')
        self.speed = random.randint(2, 5)
        self.downType = 'diamond'
        self.score = 8


class Cube(Down):
    def __init__(self):
        super().__init__(image_name_str=['source/c.png'], dead_music_str='music/cube.wav')
        self.speed = random.randint(3, 6)
        self.downType = 'cube'
        self.score = 10


class Bomb(Down):
    def __init__(self):
        super().__init__(image_name_str=['source/bo.png'], dead_music_str='music/bomb.wav')
        self.speed = random.randint(2, 5)
        self.downType = 'bomb'
        self.score = -20


class Apple(Down):
    def __init__(self):
        super().__init__(image_name_str=['source/a.png'], dead_music_str='music/apple.wav')
        self.speed = 1
        self.downType = 'apple'
        self.score = 1
