# -*- coding: utf-8 -*-

"""
@date: 2020/5/2 下午2:47
@file: util.py
@author: zj
@description: 
"""

import os
import numpy as np
import xmltodict
import torch
import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def get_device():
    return torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


def plot(log_lrs, losses):
    # x_major_locator = MultipleLocator(1)
    # ax = plt.gca()
    # ax.xaxis.set_major_locator(x_major_locator)
    fig = plt.figure()

    plt.title('loss-lr')
    plt.plot(log_lrs, losses)

    plt.savefig('./loss-lr.png')
    plt.show()
