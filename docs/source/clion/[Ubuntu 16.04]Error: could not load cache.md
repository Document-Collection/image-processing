
# Error: could not load cache

误删文件夹`cmake-build-debug`g后，重新运行提示错误：

    Error running 'Build': Cannot start process, the working directory '/home/zj/Documents/PICC/c++/cmake-build-debug' does not exist

重新新建`cmake-build-debug`，再次运行：

    ====================[ Build | c__ | Debug ]=====================================
    /home/zj/software/jetbrains/clion-2018.3.3/bin/cmake/linux/bin/cmake --build /home/zj/Documents/PICC/c++/cmake-build-debug --target c__ -- -j 4
    Error: could not load cache

参考：[Cmake Error: could not load cache](https://stackoverflow.com/questions/16319292/cmake-error-could-not-load-cache)

点击菜单栏`Tools->CMake->Reload CMake Project`s，问题解决