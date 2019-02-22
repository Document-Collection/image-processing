
# [Ubuntu 16.04][Anaconda3]Opencv-4.0.1安装

参考：[Installation in Linux](https://docs.opencv.org/4.0.1/d7/d9f/tutorial_linux_install.html)

## 4.x 变化

参考：

[Major Changes](https://github.com/opencv/opencv/wiki/Opencv4#major-changes)

[OpenCV 4.0](https://opencv.org/opencv-4-0-0.html)

`2018`年`OpenCV`发布了`4.0.1`版本，保留了`OpenCV 3.x`中绝大多数的设计原则和库布局，但同时有很多的更新，介绍其中几个

1. `OpenCV 4.0`采用`C++11`库，需要`C++11`编译器，同时最低`CMake`的版本为`3.5.1`
2. 已将二维码(`QR code`)检测器和解码器添加到`objdetect`模块中。
3. 取消了绝大多数的`1.x`版本中的`C API`。比如

对于`cvtColor`函数

    # 3.x
    cv::cvtColor(src, dst, CV_RGB2GRAY)
    # 4.x
    cv::cvtColor(src, dst, cv::COLOR_RGB2GRAY)

对于视频捕获和宽高设置

    # 3.x
    cv::VideoCapture cap(0); cap.set(CV_CAP_PROP_WIDTH, 640);
    # 4.x
    cv::VideoCapture cap(0); cap.set(cv::CAP_PROP_WIDTH, 640);

取消了`C`语言的数据结构，包括`CvMat, IplImage, CvMemStorage`，以及相对应的函数，包括`cvCreateMat(), cvThreshold()`

可是替换成`C++`的数据结构和函数，比如`cv::Mat, std::vector, cv::threshold()`

## 预配置

1. Ubuntu 16.04
2. Anaconda3

安装包

    [compiler] sudo apt-get install build-essential
    [required] sudo apt-get install cmake git libgtk2.0-dev libgtk-3-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
    [optional] sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

## 安装

下载源码

    git clone git@github.com:opencv/opencv.git

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

    -D BUILD_DOCS=ON
    -D BUILD_EXAMPLES=ON
    -D CMAKE_INSTALL_PREFIX=../install
    -D INSTALL_PYTHON_EXAMPLES=ON
    -D OPENCV_PYTHON3_VERSION=ON
    -D PYTHON3_EXECUTABLE=/home/zj/software/anaconda/anaconda3/bin/python3
    -D PYTHON3_INCLUDE_DIR=/home/zj/software/anaconda/anaconda3/include/python3.7m
    -D PYTHON3_LIBRARY=/home/zj/software/anaconda/anaconda3/lib/python3.7/config-3.7m-x86_64-linux-gnu/libpython3.7m.a
    -D PYTHON3_NUMPY_INCLUDE_DIRS=/home/zj/software/anaconda/anaconda3/lib/python3.7/site-packages/numpy/core/include/




    cmake -D CMAKE_BUILD_TYPE=RELEASE \  
        -D CMAKE_INSTALL_PREFIX=../install \  
        -D BUILD_DOCS=ON
        -D BUILD_EXAMPLES=ON
        -D INSTALL_PYTHON_EXAMPLES=ON
        -D OPENCV_PYTHON3_VERSION=ON
        -D PYTHON_EXECUTABLE=<anaconda_work_dir>/envs/<environment>/bin/python \  
        -D PYTHON_LIBRARY=<anaconda_work_dir>/envs/<environment>/lib/python2.7 \  
        -D PYTHON_INCLUDE_DIR=<anaconda_work_dir>/envs/<environment>/include/python2.7 \  
        ..
