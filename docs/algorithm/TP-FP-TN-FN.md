
# TP-FP-TN-FN

参考：

[关于false positive和false negative的定义的疑惑？](https://www.zhihu.com/question/302985367/answer/535024467)

[机器学习之分类器性能指标之ROC曲线、AUC值](https://blog.csdn.net/zdy0_2004/article/details/44948511)

[false positive 与 false negative](https://blog.csdn.net/u013264172/article/details/51972152)

## 解析

在二分类问题上，会出现以下四种分类情况

* 实例是正类
  * 预测结果是正类，称为真阳性（`true positive`，简称`TP`）
  * 预测结果是负类，称为假阴性（`false negative`，简称`FN`）
* 实例是负类
  * 预测结果是正类，称为假阳性（`false positive`，简称`FP`）
  * 预测结果是负类，称为真阴性（`true negative`，简称`TN`）

完整的计算结果如下表所示

<!-- |      |          |         预测         |                      |                  |
|:----:|:--------:|:--------------------:|:--------------------:|:----------------:|
|      |          |         true         |         false        |                  |
| 实际 | positive |   true positive(TP)  |  false positive(FP)  | 正样本个数=TP+FP |
|      | negative |   true negative(TN)  |  false negative(FN)  | 负样本个数=TN+FN |
|      |          | 预测正样本个数=TP+TN | 预测负样本个数=FP+FN |                  | -->

![](./imgs/tp-fp-tn-fn.png)

## 准确率

计算准确率（`precision rate`），指的是预测为正的样本中实际是正样本的概率，计算公式为`TP / (TP+FP)`

## 漏检率

计算漏检率（`False detection rate`），指的是实际为正样本，预测为负的概率，计算公式为`FP/(FP+TN)`

## 召回率

计算召回率（`recall rate`），指的是预测为正的正样本占整个正样本的概率，计算公式为`TP/TP+FN`