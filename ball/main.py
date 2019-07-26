# -*- coding: utf-8 -*-
# @Time    : 19-7-17 下午1:17
# @Author  : shenyingying
# @Email   : shen222ying@163.com
# @File    : main.py
# @Software: PyCharm
import pygame
from ball.down import *
from ball.basket import *
import sys


def print_text(screen, font, x, y, text, color=(240, 25, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


def make_screen():
    pygame.init()
    pygame.time.set_timer(pygame.USEREVENT, 100)
    font1 = pygame.font.Font(None, 24)
    bg_size = (800, 600)
    screen = pygame.display.set_mode(bg_size)
    background = pygame.image.load("source/back.png")
    screen.blit(background, (0, 0))

    count = 0
    Ball = []
    Ball_group = pygame.sprite.Group()
    basket = Basket(bg_size)
    protection_cover = Protection_cover(bg_size)

    while True:
        # 加载背景
        screen.blit(background, (0, 0))

        # 加载并控制篮子
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                print_text(screen, font1, 400, 0, '100ms')
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    basket.move([-1, 0])
                if event.key == pygame.K_RIGHT:
                    basket.move([1, 0])
                if event.key == pygame.K_DOWN:
                    basket.move([0, 1])
                if event.key == pygame.K_UP:
                    basket.move([0, -1])
                if event.key == pygame.K_k:
                    print_text(screen, font1, 400, 0, 'open protected')

        # print(rect)
        screen.blit(basket.default_image[0], basket.rect)

        # 加载落下的球
        for each in Ball:
            if each.disappear == True:
                Ball.remove(each)
            else:
                each.move()
                screen.blit(each.default_image[0], each.rect)

        # 检测球类和篮子是否有交集:
        for each in Ball:
            if pygame.sprite.collide_rect(each, basket):
                Ball.remove(each)
                each.inBasket()
                if each.downType == 'fireBall':
                    basket.score += each.score
        # 遇到炸弹丢一条命:
        # 当篮子的分数达到200 就 过关
        # 如果开启防护照,就不怕炸弹和火球了

        if (count % 200 == 0):
            temp = Apple()
            temp.init_image()
            temp.init_pos(random.randint(0, 800), 0)
            Ball.append(temp)
            Ball_group.add(temp)

        if (count % 500 == 0):
            temp = FireBall()
            temp.init_image()
            temp.init_pos(random.randint(0, 800), 0)
            Ball.append(temp)
            Ball_group.add(temp)

        if (count % 800 == 0):
            temp = Diamond()
            temp.init_image()
            temp.init_pos(random.randint(0, 800), 0)
            Ball.append(temp)
            Ball_group.add(temp)

        if (count % 1000 == 0):
            temp = Cube()
            temp.init_image()
            temp.init_pos(random.randint(0, 800), 0)
            Ball.append(temp)
            Ball_group.add(temp)

        if ((count + 1) % 1500 == 0):
            temp = Bomb()
            temp.init_image()
            temp.init_pos(random.randint(0, 800), 0)
            Ball.append(temp)
            Ball_group.add(temp)

        count += 1
        # print(count)
        print_text(screen, font1, 0, 0, 'score:' + str(basket.score))
        print_text(screen, font1, 750, 0, 'lives:' + str(basket.life))

        pygame.display.flip()


if __name__ == '__main__':
    make_screen()
