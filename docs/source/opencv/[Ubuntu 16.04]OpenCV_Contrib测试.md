
# [Ubuntu 16.04]OpenCV_Contrib测试

以人脸识别模块face为例，编写cmake配置文件CMakeLists.txt：

    cmake_minimum_required(VERSION 3.13)
    project(c__)

    set(CMAKE_CXX_STANDARD 14)

    set(CMAKE_PREFIX_PATH /home/zj/opencv/install)
    find_package(OpenCV REQUIRED)
    # 打印OpenCV版本
    MESSAGE("OpenCV version: ${OpenCV_VERSION}")
    # 打印OpenCV头文件地址
    MESSAGE("OpenCV include: ${OpenCV_INCLUDE_DIRS}")
    # 打印OpenCV库文件地址
    MESSAGE("OpenCV libs: ${OpenCV_LIBS}")
    # 添加include地址
    include_directories(${OpenCV_INCLUDE_DIRS})
    # 添加face模块头文件
    include_directories(/home/zj/opencv/opencv_contrib/modules)

    add_executable(c__ main.cpp OpencvDetect.cpp OpencvDetect.h Common.cpp Common.h)
    # 添加libs地址
    target_link_libraries(c__ ${OpenCV_LIBS})

**注意：face模块的头文件并没有在install安装路径下，指定到opencv_contrib/modules**

参考：[cv::face::LBPHFaceRecognizer Class Reference](https://docs.opencv.org/3.4.2/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html#a4b4903dcfaa98192784a41b299360b5c)

人脸识别结构定义在cv::face空间下，同时其头文件为facerec.hpp

新建文件OpenCVDetect.h