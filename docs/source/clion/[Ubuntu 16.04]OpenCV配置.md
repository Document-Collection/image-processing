
# [Ubuntu 16.04]OpenCV配置

`CLion`使用`cmake`作为配置工具，新建工程`first`，默认`CMakeLists.txt`如下：

    # cmake所需最低版本
    cmake_minimum_required(VERSION 3.13)
    # 工程名
    project(first)
    # 设置C++规范
    set(CMAKE_CXX_STANDARD 14)
    # 可执行文件名以及源文件
    add_executable(first main.cpp)

需要添加`OpenCV`的`include`地址以及`libs`地址，修改如下：

    cmake_minimum_required(VERSION 3.13)
    project(first)

    set(CMAKE_CXX_STANDARD 14)

    set(CMAKE_PREFIX_PATH /home/zj/opencv/debug-3.4.2--py27-py36)
    find_package(OpenCV REQUIRED)
    # 打印OpenCV版本
    MESSAGE("OpenCV version: ${OpenCV_VERSION}")
    # 添加include地址
    include_directories(${OpenCV_INCLUDE_DIRS})

    add_executable(first main.cpp)
    # 添加libs地址
    target_link_libraries(first ${OpenCV_LIBS})

源文件`main.cpp`如下

    #include <iostream>
    #include <opencv2/opencv.hpp>

    using namespace cv;
    using namespace std;

    int main() {
        std::cout << "Hello, World!" << std::endl;
        Mat img = imread("../lena.jpg");
        if (img.empty()) {
            cout << "Error" << endl;
            exit(1);
        }
        imshow("img", img);
        waitKey(0);

        return 0;
    }

**注意：生成的可执行文件在`cmake-build-debug`文件夹内，所以引用文件时注意路径**

    .
    ├── cmake-build-debug
    │   ├── CMakeCache.txt
    │   ├── CMakeFiles
    │   ├── cmake_install.cmake
    │   ├── first
    │   ├── first.cbp
    │   └── Makefile
    ├── CMakeLists.txt
    ├── lena.jpg
    └── main.cpp