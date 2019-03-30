# -*- coding: utf-8 -*-

import torch
import torch.nn as nn
import torch.nn.functional as F


class LeNet(nn.Module):
    """
    LeNet-5网络模型
    输入图像大小为1x32x32
    """

    def __init__(self):
        super(LeNet, self).__init__()
        # 卷积层
        # 1 input image channel, 6 output channels, 5x5 square convolution
        self.conv1 = nn.Conv2d(1, 6, (5, 5))
        # 池化层
        # Max pooling over a (2, 2) window
        self.pool2 = nn.MaxPool2d(2, 2)
        # If the size is a square you can only specify a single number
        # 如果滤波器是正方形，可以只输入一个数值
        self.conv3 = nn.Conv2d(6, 16, 5)
        # If the size is a square you can only specify a single number
        self.pool4 = nn.MaxPool2d(2)
        # 全连接层
        # an affine operation: y = Wx + b
        self.fc5 = nn.Linear(16 * 5 * 5, 120)
        self.fc6 = nn.Linear(120, 84)
        self.fc7 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool2(F.relu(self.conv1(x)))
        x = self.pool4(F.relu(self.conv3(x)))
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc5(x))
        x = F.relu(self.fc6(x))
        x = self.fc7(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


if __name__ == '__main__':
    net = LeNet()
    # print(net)
    inp = torch.randn(2, 1, 32, 32)
    print(inp.size())
    out = net.forward(inp)
    print(out)
    print(out.size())
