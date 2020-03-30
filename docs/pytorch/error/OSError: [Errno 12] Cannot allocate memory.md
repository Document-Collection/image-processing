
# OSError: [Errno 12] Cannot allocate memory

参考：

[死亡Error：OSError: [Errno 12] Cannot allocate memory](https://blog.csdn.net/breeze210/article/details/99679048)

[OSError: [Errno 12] Cannot allocate memory. But memory usage is actually normal](https://discuss.pytorch.org/t/oserror-errno-12-cannot-allocate-memory-but-memory-usage-is-actually-normal/56027)

执行`PyTorch`程序，发生内存不足错误

## 内存查询

监视内存，查看是否是内存不足

```
# 打开两个窗口，分别查看CPU内存和显卡内存
# 每隔1秒查询一次
$ watch -n 1 free -m
$ wathc -n 1 nvidia-smi
```

## num_workers

确实不是因为内存不足，那么修改`DataLoader`的`num_workers`为`0`，再重新运行即可

```
        num_workers (int, optional): how many subprocesses to use for data
            loading. ``0`` means that the data will be loaded in the main process.
            (default: ``0``)
```

