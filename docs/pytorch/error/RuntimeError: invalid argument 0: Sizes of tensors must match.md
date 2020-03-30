
# RuntimeError: invalid argument 0: Sizes of tensors must match except in dimension 0

参考：[12 invalid argument 0: Sizes of tensors must match except in dimension 1. Got 14 and 13 in dimension 0 at /home/prototype/Downloads/pytorch/aten/src/THC/generic/THCTensorMath.cu:83](https://oldpan.me/archives/pytorch-conmon-problem-in-training)

调用`DataSet`的`__getitem__`方法返回的`image`数据维度应该一致