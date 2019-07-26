# -*- coding: utf-8 -*-
# @Time    : 19-7-19 下午5:36
# @Author  : shenyingying
# @Email   : shen222ying@163.com
# @File    : red_road.py
# @Software: PyCharm

import pygame
import random
import sys

Yellow = (255, 255, 0)
Gray = (128, 128, 128)
Red = (255, 0, 0)

'''https://www.gameres.com/754927.html'''


def creat_random_odd(side):
    rand_pos = ((random.randint(0, 3)), (random.randint(1, int(side / 2)) * 2 - 1))
    return rand_pos


def growing_Once(base, yellow_list, red_list):
    while True:
        up = (base[0], base[1] - 2)
        right = (base[0] + 2, base[1])
        bottom = (base[0], base[1] + 2)
        left = (base[0] - 2, base[1])

        if (up in yellow_list or right in yellow_list or bottom in yellow_list or left in yellow_list):
            dir = random.randint(0, 3)  # 随机选择一个生长方向:
            if (dir == 0 and up in yellow_list):
                growing1 = (base[0], base[1] - 1)
                red_list.append(growing1)
                red_list.append(up)
                yellow_list.remove(up)
                base = up
            elif (dir == 1 and right in yellow_list):
                growing1 = (base[0] + 1, base[1])
                red_list.append(growing1)
                red_list.append(right)
                yellow_list.remove(right)
                base = right
            elif (dir == 2 and bottom in yellow_list):
                growing1 = (base[0], base[1] + 1)
                red_list.append(growing1)
                red_list.append(bottom)
                yellow_list.remove(bottom)
                base = bottom
            elif (dir == 3 and left in yellow_list):
                growing1 = (base[0] - 1, base[1])
                red_list.append(growing1)
                red_list.append(left)
                yellow_list.remove(left)
                base = left
        else:
            break

    return base, yellow_list, red_list


def get_new_base(yellow_list, red_list):
    for i in range(len(red_list)):
        base = red_list[len(red_list) - 1 - i]
        up = (base[0], base[1] - 2)
        if (up in yellow_list):
            base = up
            red_list.append(base)
            yellow_list.remove(base)
            print('up')
            break
        right = (base[0] + 2, base[1])
        if (right in yellow_list):
            base = right
            red_list.append(base)
            yellow_list.remove(base)
            print('right')
            break
        bottom = (base[0], base[1] + 2)
        if (bottom in yellow_list):
            base = bottom
            red_list.append(base)
            yellow_list.remove(base)
            print('bottom')
            break
        left = (base[0] - 2, base[1])
        if (left in yellow_list):
            base = left
            red_list.append(base)
            yellow_list.remove(base)
            print('left')
            break

    return base, yellow_list, red_list


def explore(grid, yellow_list):
    '''随机生成起点'''
    '''第一个数 是 0 ,1,2,3 {up,left,bottom,right};第二个数是 取改列或者改行任意黄点'''
    Red_list = []
    pos = creat_random_odd(grid[0])

    if (pos[0] == 0):
        start_room_point = (pos[1], 1)
        Red_list.append(start_room_point)
    elif (pos[0] == 1):
        start_room_point = (79, pos[1])
        Red_list.append(start_room_point)
    elif (pos[0] == 2):
        start_room_point = (pos[1], 79)
        Red_list.append(start_room_point)
    elif (pos[0] == 3):
        start_room_point = (1, pos[1])
        Red_list.append(start_room_point)

    '''两重循环:
    一重:首先判断当前点是否是死点,若是推出一次生长循环
    二重:判断Yellow里是否存在元素'''

    base = start_room_point

    '''开始生长'''
    count = 0
    while (len(yellow_list)):
        print('count', count)
        base, yellow_list, Red_list = growing_Once(base, yellow_list, Red_list)
        '''从red_list中找到新的可以生长的base,重新生长'''
        base, yellow_list, Red_list = get_new_base(yellow_list, Red_list)
        count += 1
    return Red_list


def drawRoom(screen, begin_point, side, classId):
    pygame.draw.rect(screen, classId, (begin_point[0], begin_point[1], side, side))


def create_base_map(grid, side):
    base_map_list = [[0] * 81 for col in range(81)]
    Yellow_list = []
    for i in range(grid[0]):
        for j in range(grid[1]):
            if (i % 2 == 1 and j % 2 == 1):
                temp_room = Room(i * side, j * side, side, Yellow)
                base_map_list[i][j] = temp_room
                temp_room_point = (i, j)
                Yellow_list.append(temp_room_point)
            else:
                base_map_list[i][j] = Room(i * side, j * side, side, Gray)
    return base_map_list, Yellow_list


class Room(object):
    def __init__(self, x, y, side, classId):
        super().__init__()
        self.x = x
        self.y = y
        self.side = side
        self.classId = classId  # {Gray Yellow Red}


def main():
    pygame.init()
    screen = pygame.display.set_mode((810, 810))
    rooms = Room(0, 0, 10, Gray)
    map_list, yellow_list = create_base_map((81, 81), 10)

    red_list = explore((81, 81), yellow_list)
    print(len(yellow_list))

    for i in range(len(map_list)):
        for j in range(len(map_list[0])):
            drawRoom(screen, (map_list[i][j].x, map_list[i][j].y), rooms.side, map_list[i][j].classId)
    for i in range(len(red_list)):
        drawRoom(screen, (red_list[i][0] * rooms.side, red_list[i][1] * rooms.side), rooms.side, Red)

    user = pygame.image.load('source/user.png').convert_alpha()
    w, h = user.get_size()
    user = pygame.transform.smoothscale(user, (8, 8))
    screen.blit(user, (10, 10))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type ==pygame.K_LEFT:
                    pass



        pygame.display.flip()


if __name__ == '__main__':
    main()
