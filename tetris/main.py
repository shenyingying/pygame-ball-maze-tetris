# -*- coding: utf-8 -*-
# @Time    : 19-7-23 上午9:30
# @Author  : shenyingying
# @Email   : shen222ying@163.com
# @File    : main.py
# @Software: PyCharm

import pygame
import random
import time
import sys

WHITE = (255, 255, 255)  # 白色
GRAY = (185, 185, 185)  # 灰色
BLACK = (0, 0, 0)  # 黑色
RED = (155, 0, 0)  # 红色
GREEN = (0, 155, 0)  # 绿色
BLUE = (0, 0, 155)  # 蓝色
YELLOW = (155, 155, 0)  # 黄色
borderColor = BLUE  # 边界颜色
bgColor = BLACK  # 背景颜色
textColor = WHITE  # 文字颜色
templateColor = (BLUE, GREEN, RED, YELLOW)  # 方块四种颜色，存于COLORS元组中

windownWidth = 640
windownHeight = 480
bg_size = (windownWidth, windownHeight)
boxsize = 20
boardWidth = 10  # 游戏窗口本身有10个方块的宽度
boardHeight = 20  # 游戏窗口本身有20个方块的高度
templateWidth = 5  # 砖块模板宽
templateHeight = 5  # 砖块模板高
blank = '.'
movesideFreq = 0.15
movedownFreq = 0.1

fps = 25

s_shape_template = [['.....',  # S逆时针变化的形状
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]
z_shape_template = [['.....',  # Z形模板
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',  # S形状的模板
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....']]
i_shape_template = [['..O..',  # I型模板
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]
o_shape_template = [['.....',  # O型模板
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

j_shape_template = [['.....',  # J型模板
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

l_shape_template = [['.....',  # L型模板
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

t_shape_template = [['.....',  # T型模板
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]
Pieces = {'s': s_shape_template,
          'z': z_shape_template,
          'j': j_shape_template,
          'l': l_shape_template,
          'i': i_shape_template,
          'o': o_shape_template,
          't': t_shape_template}
xmargin = int((windownWidth - boardWidth * boxsize) / 2)
ymargin = int((windownHeight - boardHeight * boxsize) / 2)


def main():
    global fpsclock, screen, basicFont, bigFont
    pygame.init()
    fpsclock = pygame.time.Clock()
    screen = pygame.display.set_mode(bg_size)
    basicFont = pygame.font.Font(None, 24)
    bigFont = pygame.font.Font(None, 50)
    pygame.display.set_caption('俄罗斯方块')
    showTextScreen('start game')

    while True:
        pygame.mixer.music.load('/home/sy/paper/childCode/TutorABC -python初级课件/code/ball/music/bomb.wav')
        pygame.mixer.music.play(-1, 0.0)
        play()
        pygame.mixer.music.stop()
        showTextScreen('game over')
        pygame.display.update()


def play():
    """创建一个空白的游戏板数据结构"""
    board = getBlankBoard()
    """最后按下方向键盘的时间"""
    lastMoveDownTime = time.time()
    """最后按下左右键的时间"""
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingDown = False
    movingLeft = False
    movingRight = False
    score = 0
    level, fallFreq = calculateLevelAndFallFreq(score)
    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()

    while True:
        if fallingPiece == None:
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            lastFallTime = time.time()
            if not isValidPosition(board, fallingPiece):
                return
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    """松开箭头将会把movingLeft,movingRight,movingRight变量设置城False,表示玩家不想玩了"""
                    if (event.key == pygame.K_LEFT):
                        movingLeft = False
                    elif (event.key == pygame.K_RIGHT):
                        movingRight = False
                    elif (event.key == pygame.K_DOWN):
                        movingRight = False
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT) and isValidPosition(board, fallingPiece, adjX=-1):
                        """当按下的按键为向左方向,并且向左移动一个位置有效"""
                        fallingPiece['x'] = fallingPiece['x'] - 1
                        movingLeft = True
                        movingRight = False
                        lastMoveSidewaysTime = time.time()
                    elif (event.key == pygame.K_RIGHT) and isValidPosition(board, fallingPiece, adjX=1):
                        fallingPiece['x'] = fallingPiece['x'] + 1
                        movingRight = True
                        movingLeft = False
                        lastMoveSidewaysTime = time.time()
                    elif (event.key == pygame.K_UP):
                        """按向上箭头将会把砖块旋转到下一个状态"""
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(Pieces[fallingPiece['shape']])
                        if not isValidPosition(board, fallingPiece):
                            """由于新的旋转位置与游戏板上已有的一些方块重叠而导致新的旋转位置无效,这时候需要切换到最初的旋转状态"""
                            fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(
                                Pieces[fallingPiece['shape']])
                    elif (event.key == pygame.K_DOWN):
                        movingDown = True
                        if isValidPosition(board, fallingPiece, adjY=1):
                            fallingPiece['y'] = fallingPiece['y'] + 1
                        lastMoveDownTime = time.time()
        if (movingDown or movingRight) and time.time() - lastMoveSidewaysTime > movesideFreq:
            if movingLeft and isValidPosition(board, fallingPiece, adjX=-1):
                fallingPiece['x'] = fallingPiece['x'] - 1
            elif movingRight and isValidPosition(board, fallingPiece, adjX=1):
                fallingPiece['x'] = fallingPiece['x'] + 1
            lastMoveSidewaysTime = time.time()
        if movingDown and time.time() - lastMoveDownTime > movedownFreq:
            fallingPiece['y'] = fallingPiece['y'] + 1
            lastMoveDownTime = time.time()

        """让砖块自然落下"""
        if time.time() - lastFallTime > fallFreq:
            if not isValidPosition(board, fallingPiece, adjY=1):
                addToBoard(board, fallingPiece)
                score = score + removeCompleteLine(board)
                level, fallFreq = calculateLevelAndFallFreq(score)
                fallingPiece = None
            else:
                fallingPiece['y'] = fallingPiece['y'] + 1
                lastFallTime = time.time()

        screen.fill(bgColor)
        drawBoard(board)
        drawStatus(score, level)
        drawNextPiece(nextPiece)
        if fallingPiece != None:
            drawPiece(fallingPiece)
        pygame.display.update()
        fpsclock.tick(fps)


def getBlankBoard():
    """
    创建一个新的游戏板数据
    :return:
    """
    board = []
    for i in range(boardWidth):
        board.append([blank] * boardHeight)
    return board


def isOnBoard(x, y):
    """
    :brief: 检查参数是否在游戏面板上
    :param x:
    :param y:
    :return:
    """
    return x >= 0 and x < boardWidth and y < boardHeight


def getNewPiece():
    """
    :brife:产生一个随机砖块,
    :return:
    """
    shape = random.choices(list(Pieces.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(Pieces) - 1),
                'x': int(boardWidth / 2) - int(templateWidth / 2),
                'y': -2,
                'color': random.randint(0, len(templateColor) - 1)}
    return newPiece


def addToBoard(board, piece):
    """
    :brife:游戏板块数据结构用来记录之前着陆的砖块.
           该函数所做的事情就是接受一个砖块数据结构,并且将其上的有效砖块添加到游戏板块数据结构中去
    :param board:
    :param piece:
    :return:
    """
    for x in range(templateWidth):
        for y in range(templateHeight):
            if Pieces[piece['shape']][piece['rotation']][y][x] != blank:
                board[x + piece['x']][y + piece['y']] = piece['color']
                """游戏板数据结构的值有两种形式:数字(表示砖块颜色).'.'即空白,表示该处没有有效的转块"""


def isValidPosition(board, piece, adjX=0, adjY=0):
    for x in range(templateWidth):
        for y in range(templateHeight):
            isAboveBoard = y + piece['y'] + adjY < 0
            if isAboveBoard or Pieces[piece['shape']][piece['rotation']][y][x] == blank:
                "在5*5模板中不等于'.'的方块"
                continue
            if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != blank:
                return False
    return True


def isCompleteLine(board, y):
    """
    brife:判断y行是否被填满,填满则返回True
    :param board:
    :param y:
    :return:
    """
    for x in range(boardWidth):
        if board[x][y] == blank:
            return False
    return True


def removeCompleteLine(board):
    """
    :brife:删除所有填满行,每删除一行要将游戏板上该行之上的所有方块都下移一行,返回删除的行数
    :param board:
    :return:
    """
    numLinesRemoved = 0
    y = boardHeight - 1
    while y >= 0:
        if isCompleteLine(board, y):
            for pullDownY in range(y, 0, -1):
                for x in range(boardWidth):
                    board[x][pullDownY] = board[x][pullDownY - 1]
                    "将删除行之上的每一行的值都复制到下一行"
            for x in range(boardWidth):
                board[x][0] = blank
                numLinesRemoved += 1
        else:
            y -= 1
    return numLinesRemoved


def convertToPixelCoords(boxx, boxy):
    return (xmargin + (boxx * boxsize)), (ymargin + (boxy * boxsize))


def drawBoard(board):
    pygame.draw.rect(screen, borderColor,
                     (xmargin - 3, ymargin - 7, (boardWidth * boxsize) + 8, (boardHeight * boxsize) + 8), 5)
    pygame.draw.rect(screen, bgColor, (xmargin, ymargin, boxsize * boardWidth, boxsize * boardHeight))
    for x in range(boardWidth):
        for y in range(boardHeight):
            drawBox(x, y, board[x][y])


def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
    if color == blank:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(boxx, boxy)
    pygame.draw.rect(screen, templateColor[color], (pixelx + 1, pixely + 1, boxsize - 1, boxsize - 1))


def drawPiece(piece, pixelx=None, pixely=None):
    """pixelx,pixely为5*5砖块数据结构左上角在游戏板上的坐标"""
    shapeToDraw = Pieces[piece['shape']][piece['rotation']]
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])
    for x in range(templateWidth):
        for y in range(templateHeight):
            if shapeToDraw[y][x] != blank:
                drawBox(None, None, piece['color'], pixelx + (x * boxsize), pixely + (y * boxsize))


def drawNextPiece(piece):
    nextSurf = basicFont.render('NEXT:', True, textColor)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (windownWidth - 120, 80)
    screen.blit(nextSurf, nextRect)
    drawPiece(piece, pixelx=windownWidth - 120, pixely=100)


def drawStatus(score, level):
    scoreSurf = basicFont.render('Score:%s' % score, True, textColor)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (windownWidth - 150, 20)
    screen.blit(scoreSurf, scoreRect)
    levelSurf = basicFont.render('Level:%s' % level, True, textColor)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (windownWidth - 150, 50)
    screen.blit(levelSurf, levelRect)


def showTextScreen(text):
    titleSurf, titleRect = makeTextObj(text, bigFont, textColor)
    screen.blit(titleSurf, titleRect)
    pressSurf, pressRect = makeTextObj('press a key to play', basicFont, textColor)
    screen.blit(pressSurf, pressRect)
    while checkForKeyPress() == None:
        pygame.display.update()
        fpsclock.tick()


def checkForKeyPress():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP]):
        if event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None


def calculateLevelAndFallFreq(score):
    """
    玩家每满一行,起分数都增加1,每增加10分,游戏就进入下一个关卡,砖块下落得会更快.关卡和下落的频率都是通过参数传递的
    :param score:
    :return:
    """
    level = int(score / 10) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq


def makeTextObj(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


if __name__ == '__main__':
    # print(getNewPiece()['shape'])
    main()
