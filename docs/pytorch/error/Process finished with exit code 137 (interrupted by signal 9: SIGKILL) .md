
# Process finished with exit code 137 (interrupted by signal 9: SIGKILL) 

前几天突然遇到这个问题：

```
Process finished with exit code 137 (interrupted by signal 9: SIGKILL) 
```

程序启动后被系统`KILLED`，在网上找了资料，发现是说内存不足的问题

查询内存使用情况，发现大多数内存都被缓存占据了

```
$ free -h
              total        used        free      shared  buff/cache   available
Mem:            62G         13G        450M        308M         49G         48G
Swap:          7.6G        4.2G        3.4G
```

## 额外阅读

* [Process finished with exit code 137 in PyCharm](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method)
* [multiprocessing.set_start_method(method)](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method)
* [Semaphore leaks in dataloader](https://github.com/pytorch/pytorch/issues/11727)