# -*- coding: utf-8 -*-
# @Time    : 19-7-16 下午2:57
# @Author  : shenyingying
# @Email   : shen222ying@163.com
# @File    : maze_random.py
# @Software: PyCharm

import numpy as np
import pygame
import random

Yellow = (255, 255, 0)
Gray = (128, 128, 128)
Red = (255, 0, 0)

Aqua = (0, 255, 255)
Black = (0, 0, 0)
Blue = (0, 0, 255)
Fuchsia = (255, 0, 255)
Green = (0, 128, 0)
Lime = (0, 255, 0)
Maroon = (128, 0, 0)
NavyBlue = (0, 0, 128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
White = (255, 255, 255)

color = [Aqua, Black, Blue, Fuchsia, Gray, Green, Lime, Maroon, NavyBlue, Olive, Purple, Red, Silver, Teal, Yellow]


class room(object):
    size = (40, 40)

    def __init__(self, x, y):  # 一个小房间
        # self.walls = [random.choice([True, False]), False,
        #               False, random.choice([True, False])]
        self.walls = [True, True, True, True]
        self.closed = True  # 未被开通隧道是封闭的,就是 walls = [True, True, True, True]
        self.x = x
        self.y = y

    # 一个小房间;
    def draw(self, screen, begin_point, walls, size, r_color):
        n = 0
        for wall in walls:
            x = begin_point[0]
            y = begin_point[1]
            n = n + 1
            if n == 1 and wall:
                pygame.draw.line(screen, r_color, (x, y), (x + size, y))
            if n == 2 and wall:
                pygame.draw.line(screen, r_color, (x + size, y), (x + size, y + size))
            if n == 3 and wall:
                pygame.draw.line(screen, r_color, (x + size, y + size), (x, y + size))
            if n == 4 and wall:
                pygame.draw.line(screen, r_color, (x, y + size), (x, y))

    # 建立maze的room_list;
    def creat_map(self):

        '''python 中没有二维数组,只能用列表或者字典实现二维数组
           1.暴力创建
           2.函数创建 [[0 for row in range(n)] for col in range(m)]
           3.快速创建 [([0]*3)for j in range(4)]
           4.定义一个嵌套的list [[0]*3,[0]*3,[0]*3]'''

        self.room_list = [[0] * self.size[1] for col in range(self.size[0])]  # python 生成一个m 行 n 列的二维数组
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.room_list[i][j] = room(i, j)
        return self.room_list

    def create_map_walls(self):
        '''只保证自己和邻域相通,具体在哪个方向相通 是可以随机指定的'''
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                '''首先判断自己是不是全封闭'''
                if (True):
                    '''随机产生一个方向打通,这个组成成对的邻域 可以是四邻域任何一个'''
                    open_id = random.randint(0, 3)
                    '''自己和上面房间联通,得保证上边有房间才行'''
                    '''up'''
                    if open_id == 0:
                        if j > 1:
                            self.room_list[i][j].walls[0] = False
                            self.room_list[i][j - 1].walls[2] = False
                    '''right'''
                    if open_id == 1:
                        if i < self.size[0] - 1:
                            self.room_list[i][j].walls[1] = False
                            self.room_list[i + 1][j].walls[3] = False
                    '''bottom'''
                    if open_id == 2:
                        if j < self.size[1] - 1:
                            self.room_list[i][j].walls[2] = False
                            self.room_list[i][j + 1].walls[0] = False
                    '''left'''
                    if open_id == 3:
                        if i > 1:
                            self.room_list[i][j].walls[3] = False
                            self.room_list[i - 1][j].walls[1] = False
        return self.room_list

    # 获取下一个房间;
    # def get_next_room(self):
    #     temp_rooms = {0: None, 1: None, 2: None, 3: None}
    #     count = 0
    #     # 判断上下左右四个小房间有没有被访问到,如果没被访问就加入temp_rooms
    #     # 上
    #     if (self.y > 1 and (not self.room_list[self.x][self.y - 1].visited)):
    #         temp_rooms[0] = room_list[self.x][self.y - 1]
    #         count += 1
    #
    #     # 右
    #     if (self.x < self.size[0] - 1 and (not self.room_list[self.x + 1][self.y].visited)):
    #         temp_rooms[1] = room_list[self.x + 1][self.y]
    #         count += 1
    #
    #     # 下
    #     if (self.y < self.size[1] - 1 and (not self.room_list[self.x][self.y + 1].visited)):
    #         temp_rooms[2] = room_list[self.x][self.y + 1]
    #         count += 1
    #
    #     # 左
    #     if (self.x > 1 and (not self.room_list[self.x - 1][self.y + 1].visited)):
    #         temp_rooms[3] = room_list[self.x - 1][self.y]
    #         count += 1
    #
    #     for i in range(len(temp_rooms)):
    #         if temp_rooms[i]:
    #             next_room = temp_rooms[i]
    #             next_room.x = self.x
    #             next_room.y = self.y
    #             room_id = random.randint(0, 3)
    #             if room_id == 0:
    #                 self.walls[0] = False  # 当前房间上面没墙,上面房间下面没墙
    #                 next_room.walls[2] = False
    #             if room_id == 1:
    #                 self.walls[1] = False
    #                 next_room.walls[3] = False
    #             if room_id == 2:
    #                 self.walls[2] = False
    #                 next_room.walls[0] = False
    #             if room_id == 3:
    #                 self.walls[3] = False
    #                 next_room.walls[1] = False
    #
    #             return next_room
    #     # 若没有返回next_room 说明已经走到结尾了
    #     return None
    #
    #     # if count > 0:
    #     #     do = True
    #     #     room_id = random.randint(0, 3)  # 随机生成指定某一边没有墙
    #     #     next_room = temp_rooms[room_id]
    #     #     while do:
    #     #         if temp_rooms[room_id]:
    #     #             do = False
    #     #             next_room = temp_rooms[room_id]
    #     #             if room_id == 0:
    #     #                 self.walls[0] = 0  # 当前房间上面没墙,上面房间下面没墙
    #     #                 next_room.walls[2] = 0
    #     #             if room_id == 1:
    #     #                 self.walls[1] = 0
    #     #                 next_room.walls[3] = 0
    #     #             if room_id == 2:
    #     #                 self.walls[2] = 0
    #     #                 next_room.walls[0] = 0
    #     #             if room_id == 3:
    #     #                 self.walls[3] = 0
    #     #                 next_room.walls[1] = 0
    #     #             print('next_room:', next_room.walls)
    #     #     return next_room
    #     # else:
    #     #     return None

    def creat_maze(self, next_room):
        temp_rooms = []
        while True:
            if (next_room and next_room.visited == False):
                next_room.visited = True
                temp_rooms.append(next_room)
                next_room = self.get_next_room()
                print(next_room.x, next_room.y)
            else:
                next_room = temp_rooms.pop()
                if len(temp_rooms) == 0:
                    break


# class Nacy_maze(Room):
#
#     def __init__(self):
#         super().__init__(0, 0, 10, 10, Gray)
#         self.maze_size = (810, 810)
#         self.room_size = (10, 10)
#         self.grid_size = (81, 81)
#         self.base = Gray
#         self.foreground = Yellow
#         self.road = Red
#
#     def creat_base_map(self):
#         self.base_map_list = [[0] * self.grid_size[1] for col in range(self.grid_size[0])]
#         for i in range(self.grid_size[0]):
#             for j in range(self.grid_size[1]):
#                 if (i % 2 == 1 and j % 2 == 1):
#                     self.base_map_list[i][j] = Room(i * self.room_size[0], j * self.room_size[1],
#                                                     self.room_size[0], self.room_size[0], self.foreground)
#                     pygame.draw.rect(screen, self.foreground, (i * 10, j * 10, self.room_size[0], self.room_size[0]))
#                 else:
#                     self.base_map_list[i][j] = Room(i * self.room_size[0], j * self.room_size[1],
#                                                     self.room_size[0], self.room_size[0], self.base)
#
#                     pygame.draw.rect(screen, self.base, (i * 10, j * 10, self.room_size[0], self.room_size[0]))
#
#     # def draw_base_map(self):
#     #     for i in range(self.grid_size[0]):
#     #         for j in range(self.grid_size[1]):
#     # if self.base_map_list[i][j].
#     #
#     # rooms = self.base_map_list[i][j]


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

    # def drawRoom(self, screen, begin_point, side, classId):
    #     pygame.draw.rect(screen, classId, (begin_point[0], begin_point[1], side, side))
    #
    # def create_base_map(self, grid):
    #     base_map_list = [[0] * 81 for col in range(81)]
    #     Yellow_list = []
    #     for i in range(grid[0]):
    #         for j in range(grid[1]):
    #             if (i % 2 == 1 and j % 2 == 1):
    #                 temp_room = Room(i * self.side, j * self.side,
    #                                  self.side, Yellow)
    #                 base_map_list[i][j] = temp_room
    #                 temp_room_point = (i, j)
    #                 Yellow_list.append(temp_room_point)
    #
    #             else:
    #                 base_map_list[i][j] = Room(i * self.side, j * self.side,
    #                                            self.side, Gray)
    #     return base_map_list, Yellow_list
    #
    # def explore(self, grid, yellow_list):
    #     '''随机生成起点'''
    #     '''第一个数 是 0 ,1,2,3 {up,left,bottom,right};第二个数是 取改列或者改行任意黄点'''
    #     Red_list = []
    #     pos = creat_random_odd(grid[0])
    #
    #     if (pos[0] == 0):
    #         start_room_point = (pos[1], 1)
    #         Red_list.append(start_room_point)
    #     elif (pos[0] == 1):
    #         start_room_point = (79, pos[1])
    #         Red_list.append(start_room_point)
    #     elif (pos[0] == 2):
    #         start_room_point = (pos[1], 79)
    #         Red_list.append(start_room_point)
    #     elif (pos[0] == 3):
    #         start_room_point = (1, pos[1])
    #         Red_list.append(start_room_point)
    #
    #     '''两重循环:
    #     一重:首先判断当前点是否是死点,若是推出一次生长循环
    #     二重:判断Yellow里是否存在元素'''
    #
    #     base = start_room_point
    #
    #     '''开始生长'''
    #     count = 0
    #     while (len(yellow_list)):
    #         print('count', count)
    #         base, yellow_list, Red_list = growing_Once(base, yellow_list, Red_list)
    #         '''从red_list中找到新的可以生长的base,重新生长'''
    #         base, yellow_list, Red_list = get_new_base(yellow_list, Red_list)
    #         count += 1
    #     return Red_list

    # print('execute second grows')
    # base, yellow_list, red_list = growing_Once(base, yellow_list, red_list)

    # while True:
    #
    #     up = (grow_base[0], grow_base[1] - 2)
    #     right = (grow_base[0] + 2, grow_base[1])
    #     bottom = (grow_base[0], grow_base[1] + 2)
    #     left = (grow_base[0] - 2, grow_base[1])
    #
    #     if (up in Yellow_list or right in Yellow_list or bottom in Yellow_list or left in Yellow_list):
    #         dir = random.randint(0, 3)  # 随机选择一个生长方向:
    #         if (dir == 0 and up in Yellow_list):
    #             growing1 = (grow_base[0], grow_base[1] - 1)
    #             Red_list.append(growing1)
    #             Red_list.append(up)
    #             Yellow_list.remove(up)
    #             grow_base = up
    #         elif (dir == 1 and right in Yellow_list):
    #             growing1 = (grow_base[0] + 1, grow_base[1])
    #             Red_list.append(growing1)
    #             Red_list.append(right)
    #             Yellow_list.remove(right)
    #             grow_base = right
    #         elif (dir == 2 and bottom in Yellow_list):
    #             growing1 = (grow_base[0], grow_base[1] + 1)
    #             Red_list.append(growing1)
    #             Red_list.append(bottom)
    #             Yellow_list.remove(bottom)
    #             grow_base = bottom
    #         elif (dir == 3 and left in Yellow_list):
    #             growing1 = (grow_base[0] - 1, grow_base[1])
    #             Red_list.append(growing1)
    #             Red_list.append(left)
    #             Yellow_list.remove(left)
    #             grow_base = left
    #     else:
    #         break

    # while len(Yellow_list):
    #     dir = random.randint(0, 3)  # 随机选择一个生长方向:
    #     print('dir:', dir)
    #     if (dir == 0 and grow_base[1] > 2):
    #         next = (grow_base[0], grow_base[1] - 2)
    #         if next in Yellow_list and next not in Red_list:
    #             '''把改房间类别改成red,并从 Yellow 中弹出'''
    #             growing1 = (grow_base[0], grow_base[1] - 1)
    #             Red_list.append(growing1)
    #             Red_list.append(next)
    #             Yellow_list.remove(next)
    #             grow_base = next
    #         else:
    #             dir = random.choices()
    #             continue
    #     elif (dir == 1 and grow_base[0] < 77):
    #         next = (grow_base[0] + 2, grow_base[1])
    #         if next in Yellow_list and next not in Red_list:
    #             '''把改房间类别改成red,并从 Yellow 中弹出'''
    #             growing1 = (grow_base[0] + 1, grow_base[1])
    #             Red_list.append(growing1)
    #             Red_list.append(next)
    #             Yellow_list.remove(next)
    #             grow_base = next
    #         else:
    #             continue
    #     elif (dir == 2 and grow_base[1] < 77):
    #         next = (grow_base[0], grow_base[1] + 2)
    #         if next in Yellow_list and next not in Red_list:
    #             '''把改房间类别改成red,并从 Yellow 中弹出'''
    #             growing1 = (grow_base[0], grow_base[1] + 1)
    #             Red_list.append(growing1)
    #             Red_list.append(next)
    #             Yellow_list.remove(next)
    #             grow_base = next
    #         else:
    #             continue
    #     elif (dir == 3 and grow_base[0] > 2):
    #         next = (grow_base[0] - 2, grow_base[1])
    #         if next in Yellow_list and next not in Red_list:
    #             '''把改房间类别改成red,并从 Yellow 中弹出'''
    #             growing1 = (grow_base[0] - 1, grow_base[1])
    #             Red_list.append(growing1)
    #             Red_list.append(next)
    #             Yellow_list.remove(next)
    #             grow_base = next
    #         else:
    #             continue
    #     else:
    #         continue

    # print(pos)
    # print(start_room.x, start_room.y)


class A(object):
    def __init__(self, x, y):
        self.pos = (x, y)
        super().__init__()

    def creat(self):
        list_map = []
        for i in range(3):
            a = A(i, 0)
            list_map.append((i, 0))
        return list_map


if __name__ == '__main__':

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

    while True:
        pygame.display.flip()

    '''https://blog.csdn.net/qq_41556318/article/details/85880546'''

    #pygame a = A(0, 0)
    # a_map = a.creat()
    # print(type(a_map[0]))
    # a = (0, 0)
    # if a in a_map:
    #     print('ok')
    # for i in range(len(yellow_list)):
    #     rooms.drawRoom(screen, (yellow_list[i][0] * rooms.side, yellow_list[i][1] * rooms.side), rooms.side, Red)
    # print(yellow_list[0].x)
    # rooms111 = (1, 1)
    # if rooms111 == yellow_list[0]:
    #     print('ok')
