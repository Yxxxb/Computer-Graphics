# -*- coding:utf-8 -*-
"""
Author :Yxxxb
Date   :2021/09/17
File   :Transform.py
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# 读图片 resize 便于操作
img = cv2.imread('./img/tiger.jpg')
img_tiger = cv2.resize(img, (1024, 1024))
img_tiger = cv2.cvtColor(img_tiger, cv2.COLOR_RGB2BGR)
img = cv2.imread('./img/cat.jpg')
img_cat = cv2.resize(img, (1024, 1024))
img_cat = cv2.cvtColor(img_cat, cv2.COLOR_RGB2BGR)
plt.imshow(np.hstack([img_tiger, img_cat]))

# 设置权重函数 输出图片
for i in range(21):
    img_fusion = i / 20 * img_tiger + (20 - i) / 20 * img_cat
    img_fusion = img_fusion.astype(np.uint8)
    cv2.imwrite(f'./ans/transform{i + 1}.png', cv2.cvtColor(img_fusion, cv2.COLOR_BGR2RGB))
    plt.imshow(img_fusion)
    plt.show()
