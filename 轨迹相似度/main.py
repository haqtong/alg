# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
import json
import math

# np.random.seed(913)
fn = sys.argv[0].split('/')[-1].split('.')[0]
filename = 'log/' + sys.argv[0].split('/')[-1].split('.')[0] + '.log'

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename=filename, level=logging.INFO, format=LOG_FORMAT)


def exec():
    frechet() #弗雷歇距离
    HMM() # Hidden Markov Model 隐马尔可夫模型




if __name__ == '__main__':
    exec()