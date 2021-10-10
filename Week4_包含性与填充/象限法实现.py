# -*- coding:utf-8 -*-
"""
Author :Yxxxb & Xubing Ye
Number :1953348
Date   :2021/10/09
File   :象限法实现.py
"""

import matplotlib.pyplot as plt


def drawline(x, y):
    for i in range(len(x)):
        plt.plot(x[i], y[i], color='r')
        plt.scatter(x[i], y[i], color='b')


def tellLocation(x, y):
    assert (x != 0 and y != 0)
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


def calChange(x, y):
    if y[1] * x[0] - x[1] * y[0] > 0:
        return 1
    elif y[1] * x[0] - x[1] * y[0] > 0:
        return -1
    else:
        return 0


def cal(x, y):
    ans = 0
    for i in range(len(x)):
        Loc1 = tellLocation(x[i][0], y[i][0])
        Loc2 = tellLocation(x[i][1], y[i][1])
        if abs(Loc1 - Loc2) == 0:
            pass
        elif abs(Loc1 - Loc2) == 2:
            ans = ans + calChange(x[i], y[i])
        elif Loc1 - Loc2 == 1 or Loc1 - Loc2 == -3:
            ans = ans - 0.5
        else:
            ans = ans + 0.5
    assert (ans == 0 or ans == 1 or ans == 2)
    explain = {
        0: "在外部",
        1: "在边界上",
        2: "在内部"
    }
    return ans, explain.get(ans)


xList = [[2, -4], [-4, -4], [-4, 4], [4, 4], [4, -2], [-2, 2]]
yList = [[4, 4], [4, -4], [-4, -4], [-4, 2], [2, -2], [-2, 4]]

xList1 = [[4, -4], [-4, 1], [1, -2], [-2, 4], [4, 4]]
yList1 = [[4, 4], [4, 3], [3, -4], [-4, -4], [-4, 4]]

plt.scatter(0, 0, color='black')
drawline(xList, yList)

# plt.plot([-2, 0], [-2, 0], color='black', linestyle=':')
# plt.plot([0, 2], [0, 4], color='black', linestyle=':')
plt.plot([-5, 5], [0, 0], color='black', linestyle=':')
plt.plot([0, 0], [-5, 5], color='black', linestyle=':')

plt.show()

print(cal(xList, yList))
