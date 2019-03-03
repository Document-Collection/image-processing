
# [Ubuntu 16.04]OpenCV-4.0.1测试

参考:[[Ubuntu 16.04]OpenCV-3.4测试](https://zj-image-processing.readthedocs.io/zh_CN/latest/opencv/[Ubuntu%2016.04]OpenCV%E6%B5%8B%E8%AF%95.html)

和之前`OpenCV`版本不同,`OpenCV-4.0.1`使用`c++11`,所以需要在配置文件中指定编译环境

## `cmake`

参考:[cmake增加C++11](https://blog.csdn.net/sinat_21190681/article/details/83508228)

    $ cat CMakeLists.txt
    cmake_minimum_required(VERSION 2.8)
    # 指定c++11
    add_definitions(-std=c++11)
    project( DisplayImage )
    find_package( OpenCV REQUIRED )
    MESSAGE("OpenCV version: ${OpenCV_VERSION}")
    include_directories( ${OpenCV_INCLUDE_DIRS} )
    add_executable( DisplayImage DisplayImage.cpp )
    target_link_libraries( DisplayImage ${OpenCV_LIBS} )

## `make`

    $ cat makefile 
    INCLUDE=$(shell pkg-config --cflags opencv)
    LIB=$(shell pkg-config --libs opencv)
    SOURCE=DisplayImage.cpp
    RES=DisplayImage

    $(RES):$(SOURCE)
        g++ -std=c++11 $(SOURCE) $(INCLUDE) $(LIB) -o $(RES)

    clean:
        rm $(RES)

### 错误

参考:[Linux locate ldconfig pkg-config ldd 以及 OpenCV C++库的使用](https://blog.csdn.net/u012005313/article/details/82350430#T2)

    $ ./DisplayImage lena.jpg 
    ./DisplayImage: error while loading shared libraries: libopencv_highgui.so.4.0: cannot open shared object file: No such file or directory

系统找不到动态库,需要配置进行动态库的绑定,在路径`/etc/ld.so.conf.d`下新建配置文件`opencv.conf`并刷新

    $ sudo vim opencv.conf
    /home/zj/opencv/opencv-4.0.1/install/lib
    $ sudo ldconfig