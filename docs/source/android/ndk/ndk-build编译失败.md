
# ndk-build编译失败

## 问题一

    /home/zj/Android/Sdk/ndk-bundle/build/ndk-build
    Android NDK: android-8 is unsupported. Using minimum supported version android-16.    
    Android NDK: WARNING: APP_PLATFORM android-16 is higher than android:minSdkVersion 1 in /home/zj/Documents/PICC/android/numberocr/src/main/AndroidManifest.xml. NDK binaries will *not* be compatible with devices older than android-16. See https://android.googlesource.com/platform/ndk/+/master/docs/user/common_problems.md for more information.    
    Android NDK: ERROR:/home/zj/Documents/PICC/android/numberocr/src/main/jni/Android.mk:opencv_contrib: LOCAL_SRC_FILES points to a missing file    
    Android NDK: Check that /home/zj/Android/OpenCV-android-sdk/sdk/native/jni/../libs/arm64-v8a/libopencv_contrib.a exists  or that its path is correct   
    /home/zj/Android/Sdk/ndk-bundle/build/core/prebuilt-library.mk:45: *** Android NDK: Aborting    .  Stop.

查找`arm64-v8a/libopencv_contrib.a`是否存在，设置`Application.mk`编译平台为

    APP_ABI := armeabi-v7a

## 问题二

    /home/zj/Android/Sdk/ndk-bundle/build/ndk-build
    Android NDK: android-8 is unsupported. Using minimum supported version android-16.    
    Android NDK: WARNING: APP_PLATFORM android-16 is higher than android:minSdkVersion 1 in /home/zj/Documents/PICC/android/numberocr/src/main/AndroidManifest.xml. NDK binaries will *not* be compatible with devices older than android-16. See https://android.googlesource.com/platform/ndk/+/master/docs/user/common_problems.md for more information.    
    Android NDK: WARNING:/home/zj/Documents/PICC/android/numberocr/src/main/jni/Android.mk:IDNumberOCR: non-system libraries in linker flags: -latomic    
    Android NDK:     This is likely to result in incorrect builds. Try using LOCAL_STATIC_LIBRARIES    
    Android NDK:     or LOCAL_SHARED_LIBRARIES instead to list the library dependencies of the    
    Android NDK:     current module    
    /home/zj/Documents/PICC/android/numberocr/src/main/obj/local/armeabi-v7a/objs/IDNumberOCR/main.o.d:1: *** target pattern contains no `%'.  Stop.

参考：[android ndk-build 时出现target pattern contain no % 的解决方法](https://blog.csdn.net/onerain88/article/details/6969235)

删除obj文件夹（这个文件夹伴随着libs一起生成）里的.o文件，重新ndk-build即可

## 问题三

    7:14: fatal error: 'array' file not found

参考：[解决ndk-build : fatal error: 'iostream' file not found](https://blog.csdn.net/liangtianmeng/article/details/83511480)

新建Application.mk，添加

    APP_STL := c++_static
