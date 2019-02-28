
# dlopen failed: library "libopencv_java3.so" not found

问题描述

    2019-02-28 20:11:25.855 17090-17090/com.zj.picc E/AndroidRuntime: FATAL EXCEPTION: main
        Process: com.zj.picc, PID: 17090
        java.lang.UnsatisfiedLinkError: dlopen failed: library "libopencv_java3.so" not found

参考：[Unable to link native library in OpenCV Android sample](https://stackoverflow.com/questions/10857301/unable-to-link-native-library-in-opencv-android-sample/29640808#29640808)

我用的`opencv-android-sdk`版本是`3.4.2`，搜索是否包含`libopencv_java3.so`

    $ locate libopencv_java3.so
    /home/zj/Android/OpenCV-android-sdk/sdk/native/libs/arm64-v8a/libopencv_java3.so
    /home/zj/Android/OpenCV-android-sdk/sdk/native/libs/armeabi/libopencv_java3.so
    /home/zj/Android/OpenCV-android-sdk/sdk/native/libs/armeabi-v7a/libopencv_java3.so
    /home/zj/Android/OpenCV-android-sdk/sdk/native/libs/mips/libopencv_java3.so
    /home/zj/Android/OpenCV-android-sdk/sdk/native/libs/mips64/libopencv_java3.so
    /home/zj/Android/OpenCV-android-sdk/sdk/native/libs/x86/libopencv_java3.so
    /home/zj/Android/OpenCV-android-sdk/sdk/native/libs/x86_64/libopencv_java3.so

将对应版本(`arm64-v8a、armeabi-v7a`)的`libopencv_java3.so`文件复制到`libs`文件夹下，同时修改加载静态库代码

    static {
        System.loadLibrary("opencv_java3");
        System.loadLibrary("NumberOCR");
    }