# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
import json
import math
from shapesimilarity import shape_similarity
import matplotlib.pyplot as plt

class shapeSimilarity:
    def __init__(self):
        pass

    def frechet(self):
        '''
        输入是什么
        :return:
        '''
        x = np.linspace(1, -1, num=200)

        y1 = 2 * x ** 2 + 1
        y2 = 2 * x ** 2 + 2

        shape1 = np.column_stack((x, y1))
        shape2 = np.column_stack((x, y2))

        print(shape1)
        print(shape2)

        similarity = shape_similarity(shape1, shape2)

        plt.plot(shape1[:, 0], shape1[:, 1], linewidth=2.0)
        plt.plot(shape2[:, 0], shape2[:, 1], linewidth=2.0)

        plt.title(f'Shape similarity is: {similarity}', fontsize=14, fontweight='bold')
        plt.show()

    def LIP(self):

        pass

    def LCSS(self):


if __name__ == '__main__':
    SS = shapeSimilarity()
    SS.frechet()


# 曲线的输入是什么 -》点位的二维数组

# 以上图为例，归一化以后，在未平移前，完全没有交叉的区域

# 要求数据等节点
