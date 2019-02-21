
# [Ubuntu 16.04][Anaconda3]Opencv-4.0.1安装

参考：[Installation in Linux](https://docs.opencv.org/4.0.1/d7/d9f/tutorial_linux_install.html)

## 预配置

1. Ubuntu 16.04
2. Anaconda3

需要的包

    [compiler] sudo apt-get install build-essential
    [required] sudo apt-get install cmake git libgtk2.0-dev libgtk-3-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
    [optional] sudo apt-get install libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

## 安装

下载源码[OpenCV-4.0.1](https://github.com/opencv/opencv/releases/tag/4.0.1)

解压生成opencv-4.0.1

    $ cd opencv/opencv-4.0.1/
    $ mkdir build
    $ mkdir install
    $ cd build

仅编译C++库 

    # 生成编译文件，设置编译版本为release，指定安装包前缀
    $ cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=../install ..
    
同时编译Python库

$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=../install \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=ON \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
	-D BUILD_EXAMPLES=ON ..
