
# Tensor

参考:[WHAT IS PYTORCH?](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py)

`Tensor`(张量)是`pytorch`最重要的数据结构,类似与`numpy`库中的`ndarray`,能够实现多维数据的加/减/乘/除以及更加复杂的操作

1. 创建`tensor`
2. 加/减/乘/除
3. 矩阵运算
4. 访问元素
5. `in_place`操作
6. `numpy`格式转换
7. `cuda tensor`

`tensor`函数查询:[TORCH](https://pytorch.org/docs/stable/torch.html)

## 创建`tensor`

创建一个`5`行`3`列的`tensor`

    # 赋值为0
    torch.zeros(5, 3)
    # 赋值为1
    torch.ones(5, 3)
    torch.new_ones(5, 3)
    # 未初始化
    torch.empty(5, 3)
    # 赋值均匀分布的随机数,大小在[0,1)
    torch.rand(5, 3)
    torch.randn_like(5, 3)

也可以转换列表为`tensor`

    torch.tensor([[0 for i in range(3)] for j in range(5)])

或者复制其他`tensor`

    # 复制张量的大小一致
    w=torch.ones(3,2)
    w.copy_(x)

### 设置数据类型

在创建`tensor`的同时设置数据类型,比如

    torch.zeros(5, 3, dtype=torch.float)
    # 或
    torch.tensor([[1 for i in range(3)] for j in range(5)], dtype=torch.float)

常用数据类型包括

* `torch.float`
* `torch.double`

### 获取大小

    $ x = tensor.zeros(5, 3)
    $ x.size()
    torch.Size([5, 3])

`torch.Size`类型实际上是一个元组(`tuple`),可以执行所有元组操作

## 加/减/乘/除

进行加/减/乘/除的张量大小相同,在对应位置上进行操作

    x = torch.ones(2, 3)
    y = torch.randn(2, 3)
    # 加
    torch.add(x, y)
    # 减 x - y
    torch.sub(x, y)
    # 乘
    torch.mul(x, y)
    # 除 x / y
    torch.div(x,y)

## 矩阵运算

    # 转置
    x = torch.ones(2,3) # 生成一个2行3列
    y = x.t()           # 得到一个3行2列

## 访问元素

可以执行类似`Numpy`数组的取值操作

    x = torch.tensor([x for x in range(6)])
    print(x)
    print(x[0])
    print(x[:3])
    # 结果
    tensor([0, 1, 2, 3, 4, 5])
    tensor(0)
    tensor([0, 1, 2])

使用函数`item()`将单个`tensor`转换成数值(标量,`scalar`)

    print(x[3].item())
    3

## `in_place`操作

`tensor`可以执行`in_place`操作,只需要在函数末尾添加下划线

    # 加
    x.add_(y)
    # 减
    x.sub_(y)
    # 转置
    x.t_()

## `numpy`格式转换

`torch`支持`tensor`和`numpy`数组的转换

`tensor`转换为`numpy`

    a = torch.ones(5)
    b = a.numpy()

`numpy`转换成`tensor`

    import numpy as np
    a = np.ones(5)
    b = torch.from_numpy(a)

除了`CharTensor`以外,`CPU`上的其他`Tensor`都支持和`Numpy`的转换

## `cuda tensor`

利用`CUDA`调用`GPU`进行`tensor`运算,需要使用函数`to`进行`GPU`和`CPU`的转换

    x = torch.tensor(5)
    if torch.cuda.is_available():                # 测试cuda是否有效
        device = torch.device("cuda")            # 生成一个cuda对象
        y = torch.ones_like(x, device=device)    # 在GPU中创建y
        x = x.to(device)                         # 在GPU中创建x
        z = x + y                                # GPU运算
        print(x)
        print(y)
        print(z)
        print(z.to('cpu', torch.double))         # 在CPU中创建z