# -*- coding:utf-8 -*-
"""
Author :Yxxxb & Xubing Ye
Number :1953348
Date   :2021/09/26
File   :Draw.py
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


def draw_point(img, x, y):
    img[x, y] = 0


def show_image(img, name):
    temp_img = cv2.cvtColor(img * 255, cv2.COLOR_GRAY2BGR)
    plt.title(name)
    plt.imshow(temp_img)
    plt.savefig(f'./out/output_{name}.png')  # Attention (save在show前)
    plt.show()


# DDA
def DDA(img, x1, y1, x2, y2):
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    k = (y2 - y1) / (x2 - x1)
    for i in range(x1, x2):
        draw_point(img, i, y1)
        y1 = round(y1 + k)


# 线有宽度
def WidLineDDA(img, x1, y1, x2, y2):
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    k = (y2 - y1) / (x2 - x1)
    width = 10 * 2
    half_width = int(round(width / 2))
    for i in range(x1, x2):
        # 两条基准线
        # cv2.circle(img, (i, int(y0 + 0.5 - half_width)), 1, (255, 255, 255), 1)
        # cv2.circle(img, (i, int(y0 + 0.5 + half_width)), 1, (255, 255, 255), 1)

        for j in range(-half_width, half_width):
            draw_point(img, i, round(y1) + j)

        y1 = y1 + k


# Bresenham
def Bresenham(img, x1, y1, x2, y2):
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    dx = x2 - x1
    dy = y2 - y1
    assert dy / dx <= 1

    D = 2 * dy - dx
    y = y1

    for x in range(x1, x2 + 1):
        if (x >= 0 and x < 500 and y >= 0 and y < 500):
            draw_point(img, x, y)
        if D > 0:
            y += 1
            D -= 2 * dx
        D += 2 * dy


# 中点画圆
def DrawEightPartCircle(img, xc, yc, addx, addy):
    draw_point(img, xc + addx, yc + addy)
    draw_point(img, xc + addx, yc - addy)
    draw_point(img, xc + addy, yc + addx)
    draw_point(img, xc + addy, yc - addx)
    draw_point(img, xc - addx, yc + addy)
    draw_point(img, xc - addx, yc - addy)
    draw_point(img, xc - addy, yc + addx)
    draw_point(img, xc - addy, yc - addx)


def MidCircle(img, xc, yc, r):
    p = 1 - r
    addx = 0
    addy = r
    DrawEightPartCircle(img, xc, yc, addx, addy)
    while addx < addy:
        addx += 1
        if p < 0:
            p += 2 * addx + 1
        else:
            addy -= 1
            p += 2 * (addx - addy) + 1
        DrawEightPartCircle(img, xc, yc, addx, addy)


# 椭圆画法 (核心思想 找到变化临界点：法向量45°)
def DrawFourPartOval(img, x, y):
    draw_point(img, x + 250, y + 250)
    draw_point(img, x + 250, -y + 250)
    draw_point(img, -x + 250, y + 250)
    draw_point(img, -x + 250, -y + 250)


def MidOval(img, a, b):
    x = 0
    y = b
    d1 = b * b + a * a * (-b + 0.25)  # 增量初值
    draw_point(img, x, y)
    draw_point(img, x, -y)

    while (b * b * (x + 1) < a * a * (y - 0.5)):
        if d1 < 0:
            d1 += b * b * (2 * x + 3)
            x += 1
        else:
            d1 += b * b * (2 * x + 3) + a * a * (-2 * y + 2)
            x += 1
            y -= 1
        DrawFourPartOval(img, x, y)

    # 椭圆弧的下半部分
    d2 = b * b * (x + 0.5) * (x + 0.5) + a * a * (y - 1) * (y - 1) - a * a * b * b
    while y > 0:  # 终结条件y>0
        if d2 < 0:
            d2 += b * b * (2 * x + 2) + a * a * (-2 * y + 3)
            x += 1
            y -= 1
        else:
            d2 += a * a * (-2 * y + 3)
            y -= 1
        DrawFourPartOval(img, x, y)


if __name__ == '__main__':
    image = []
    idx = 0

    image.append(np.ones([500, 500], dtype=np.uint8))
    DDA(image[idx], 15, 100, 200, 480)
    show_image(image[idx], "DDA")
    idx += 1

    image.append(np.ones([500, 500], dtype=np.uint8))
    WidLineDDA(image[idx], 30, 30, 450, 100)
    show_image(image[idx], "Line with width by DDA")
    idx += 1

    image.append(np.ones([500, 500], dtype=np.uint8))
    Bresenham(image[idx], 175, 250, 450, 450)
    show_image(image[idx], "Bresenham")
    idx += 1

    image.append(np.ones([500, 500], dtype=np.uint8))
    MidCircle(image[idx], 250, 250, 100)
    show_image(image[idx], "MidCircle")
    idx += 1

    image.append(np.ones([500, 500], dtype=np.uint8))
    MidOval(image[idx], 160, 220)
    show_image(image[idx], "MidOval")
    idx += 1
