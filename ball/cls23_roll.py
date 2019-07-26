import pygame
import sys
import random
import cv2





def playGame(val, screen, screen_w, screen_h, lives, score):
    font1 = pygame.font.Font(None, 24)
    rect_x, rect_y, rect_w, rect_h = 300, 460, 120, 40
    ball_x, ball_y = random.randint(0, 500), -50
    vel_y = 1 + score / 10
    white = 255, 255, 255
    while lives > 0:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # elif event.type == pygame.MOUSEMOTION:
            #     rect_x, rect_y = event.pos
            #     if rect_x < 0:
            #         rect_x = 0
            #     elif rect_x > screen_w - rect_w:
            #         rect_x = screen_w - rect_x

            # elif event.type ==pygame.KEYDOWN:
            #     if event.type==pygame.K_LEFT:
            #          rect_x += 20
            #     elif event.type == pygame.K_RIGHT:
            #         rect_x -= 20

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            elif keys[pygame.K_RIGHT]:
                rect_x += 40
            elif keys[pygame.K_LEFT]:
                rect_x -= 40

        screen.fill(white)
        pygame.draw.rect(screen, (50, 0, 0), (rect_x, rect_y, rect_w, rect_h), 0)
        if ball_y > screen_h:
            lives -= 1
            ball_x = random.randint(0, screen_w)
            ball_y = -1
        elif (ball_y - rect_y) < 30 and ball_x > rect_x and ball_x < (rect_x + rect_w):
            score += 1
            ball_x = random.randint(0, screen_w)
            ball_y = -1
        else:
            ball_y += vel_y
        pygame.draw.circle(screen, (125, 100, 210), (int(ball_x), int(ball_y)), 30, 0)
        print_text(screen, font1, 0, 0, "lives:" + str(lives))
        print_text(screen, font1, screen_w - 100, 0, "scores:" + str(score))
        pygame.display.update()
    return lives, score


def update_basket():
    global basket_x, basket_y
    basket_x, ignore = pygame.mouse.get_pos()
    basket_x


def main():
    pygame.init()
    screen_w, screen_h = 800, 600
    screen = pygame.display.set_mode((screen_w, screen_h))
    val = 1
    pygame.display.set_caption("BALL")
    # background = pygame.image.load('source/ball.png')
    basket = pygame.image.load("source/b.png")
    basket_w, basket_h = basket.get_size()
    ball = pygame.image.load("source/ball.png")
    ball_w, ball_h = ball.get_size()
    screen.blit(basket, (100, 600 - basket_h))

    font1 = pygame.font.Font(None, 24)
    lives = 10
    score = 0
    while True:
        lives, score = playGame(val, screen, screen_w, screen_h, lives, score)
        # screen.blit(background, (0, 0))
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP:
                lives = 10
                score = 0
        print_text(screen, font1, 200, 300, 'score:' + str(score) + '<replay>')
        pygame.display.flip()


SCREEN_RECT = pygame.Rect(0, 0, 800, 600)
FRAM_PER_SEC = 100
CREAT_BALL_EVENT = pygame.USEREVENT

from ball.down import *
from ball.basket import *
import sys

def print_text(screen, font, x, y, text, color=(240, 25, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

def make_screen():
    pygame.init()
    font1 = pygame.font.Font(None, 24)
    bg_size = (800, 600)
    screen = pygame.display.set_mode(bg_size)
    background = pygame.image.load("source/back.png")
    screen.blit(background, (0, 0))

    count = 0
    Ball = []
    Ball_group = pygame.sprite.Group()
    basket = Basket(bg_size)

    while True:
        # 加载背景
        screen.blit(background, (0, 0))

        # 加载并控制篮子
        for event in pygame.event.get():
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
                # if event.key == pygame.K_k:
                #     print_text(screen, font1, 400, 0, 'open protected')
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


def test_rect():
    screen = pygame.display.set_mode((800, 600))
    white = (255, 255, 255)
    screen.fill(white)
    background = pygame.image.load("/home/sy/paper/childCode/TutorABC -python初级课件/code/ball/source/a.png")
    rect = background.get_rect()
    screen.blit(background, (10, 20, rect.height, rect.width))
    print(rect.bottom)
    print(rect.right)
    print(rect.width)
    print(rect.height)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rect = rect.move(20, 0)
                if event.key == pygame.K_RIGHT:
                    rect = rect.move(-20, 0)
        screen.fill(white)
        screen.blit(background, rect)
        pygame.display.flip()

        pygame.display.flip()


if __name__ == '__main__':
    # test_rect()
    make_screen()
