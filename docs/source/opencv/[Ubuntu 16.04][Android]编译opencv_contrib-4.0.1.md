
# [Ubuntu 16.04][Android]编译opencv_contrib-4.0.1

最新的cmake

最新的ninja

opencv opencv_contrib 4.0.1

android sdk ndk

no ccache有什么用

1. ANDROID_STL gnustl_shared 和 c++_shared

2. 禁止安装ANDROID prject

3. 添加动态库 build_shared_libs

4. 指定交叉编译配置文件 /path/to/build/cmake/

cmake版本:3.14.0-rc3

ninja:1.8.2

ndk:android-ndk-r18b

