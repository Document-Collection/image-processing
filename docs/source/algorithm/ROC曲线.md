
# ROC曲线

参考：[Receiver operating characteristic](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)

`ROC`曲线，全称是接受者操作特征曲线（`receiver operating characteristic curve`），能够证明在不同阈值条件下二值分类器的检测性能

## true positive rate

参考：[Sensitivity and specificity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity)

`ROC`曲线的`y`轴表示真阳性率（`true positive rate(TPR)`），也称为召回率（`recall rate`）或者检测率（`probability of detection`）

`TPR`计算的是预测为正的正样本（`true positive`）个数占整个正样本的比例，计算公式为`TPR = TP / (TP+FN)`

## false positive rate

参考：[False positive rate](https://en.wikipedia.org/wiki/False_positive_rate)

`ROC`曲线的`x`轴表示假阳性率（`false positive rate(FPR)`），也称为误报率（`probability of false alarm`）

`FPR`计算的是预测为负的正样本（`false positive`）个数占整个负样本的比例，计算公式为`FPR = FP / (FP+TN)`

## 解析

最好的检测效果位于坐标点(0,1)，指的是所有正样本都被检测为正，没有负样本