# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
import json
import math

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='afc.log', level=logging.INFO, format=LOG_FORMAT)


# -*- coding:utf-8 -*-
# Author:   liyanpeng
# Email:    liyanpeng@tsingmicro.com
# Datetime: 2023/5/6 14:59
# Filename: ant_colony_optimization.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from base_algorithm import BaseAlgorithm


__all__ = ['AntColonyOptimization']


class Ant:
    def __init__(self):
        self.position = None    # 蚂蚁的位置
        self.tau = None         # 蚂蚁的信息素
        self.tran_prob = None   # 状态转移概率


class AntColonyOptimization(BaseAlgorithm):
    def __init__(self, population_size=20, max_iter=200, alpha=1.5, beta=0.8, rho=0.9, q=1.0, p0=0.2, step=0.1, x_range=(0, 5), seed=10086):
        super(AntColonyOptimization, self).__init__()
        self.__population_size = population_size  # 蚂蚁种群大小
        self.__max_iter = max_iter  # 最大迭代次数
        self.__alpha = alpha        # 信息素重要程度因子
        self.__beta = beta          # 启发函数重要程度因子
        self.__rho = rho            # 信息素蒸发系数
        self.__q = q                # 信息素释放增量系数
        self.__p0 = p0              # 转移概率常数
        self.__step = step          # 局部搜索步长
        self.__x_range = x_range    # 变量x的定义域
        self.__population = []      # 蚁群
        self.__best_tau = np.inf
        self.__seed = seed
        self.optimal_solution = None

        np.random.seed(seed)

    def init_population(self):
        for i in range(self.__population_size):
            ant = Ant()
            ant.position = np.random.uniform(*self.__x_range)   # 随机初始化位置
            ant.tau = self.problem_function(ant.position)       # 初始信息素值
            if ant.tau < self.__best_tau:
                self.__best_tau = ant.tau
            self.__population.append(ant)

        for ant in self.__population:
            # 初始蚂蚁的状态转移概率
            ant.tran_prob = (self.__best_tau - ant.tau) / self.__best_tau

    def update_population(self, coef):
        for ant in self.__population:
            if ant.tran_prob < self.__p0:   # 局部搜索
                new_pos = ant.position + (2 * np.random.randn() - 1) * self.__step * coef
            else:                           # 全局搜索
                new_pos = ant.position + (self.__x_range[1] - self.__x_range[0]) * (np.random.randn() - 0.5)
            new_pos = np.clip(new_pos, *self.__x_range)

            if self.problem_function(new_pos) < self.problem_function(ant.position):
                # 更新蚂蚁的位置
                ant.position = new_pos

        for ant in self.__population:
            # 更新蚂蚁的信息素
            ant.tau = (1 - self.__rho) * ant.tau + self.problem_function(ant.position)
            if ant.tau < self.__best_tau:
                self.__best_tau = ant.tau
                self.optimal_solution = (ant.position, self.problem_function(ant.position))

    def solution(self):
        self.init_population()
        for i in range(self.__max_iter):
            coef = 1 / (i+1)
            self.update_population(coef)

        print('the optimal solution is', self.optimal_solution)


if __name__ == '__main__':
    algo = AntColonyOptimization()
    algo.solution()
