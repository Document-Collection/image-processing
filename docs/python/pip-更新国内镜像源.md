
# [pip]更新国内镜像源

同事推荐为`pip`配置国内镜像源，确实很有效，对于一些常用的`python`库来说能够极大的加快下载速度

参考：[Python pip 修改镜像源为豆瓣源](https://www.douban.com/note/672475302/)

## 配置

修改配置文件`~/.pip/pip.conf`，添加

```
[global]
index-url = https://pypi.doubanio.com/simple
trusted-host = pypi.doubanio.com
```