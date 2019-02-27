# [Ubuntu 16.04]制作启动器

参考：[[Ubuntu 16.04]启动器制作](https://zj-linux-guide.readthedocs.io/zh_CN/latest/system-related/[Ubuntu%2016.04]%E5%90%AF%E5%8A%A8%E5%99%A8%E5%88%B6%E4%BD%9C.html)

使用工具`gnome-desktop-item-edit`创建桌面启动器

    $ gnome-desktop-item-edit --create-new ~/Desktop/

![](./imgs/create_launcher.png)

输入名字，指定启动脚本`studio.sh`，点击图标指定图片，还可以输入备注

![](./imgs/as-launcher.png)

这样在桌面就生成了启动器，点击即可启动`Android Studio`

## 搜索栏设置

将生成的启动器`as.desktop`放置到`~/.local/share/applications`，即可在搜索栏中找到