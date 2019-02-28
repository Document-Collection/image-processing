
# [Ubuntu 16.04]android studio配置javah和ndk-build

首先下载OpenCV Android sdk库

编辑Android.mk

    LOCAL_PATH := $(call my-dir)

    include $(CLEAR_VARS)

    ifdef OPENCV_ANDROID_SDK
    ifneq ("","$(wildcard $(OPENCV_ANDROID_SDK)/OpenCV.mk)")
        include ${OPENCV_ANDROID_SDK}/OpenCV.mk
    else
        include ${OPENCV_ANDROID_SDK}/sdk/native/jni/OpenCV.mk
    endif
    else
    include /home/zj/Android/OpenCV-android-sdk/sdk/native/jni/OpenCV.mk
    endif

    LOCAL_SRC_FILES  := main.cpp ocrutil.cpp ocr.cpp
    LOCAL_C_INCLUDES += $(LOCAL_PATH)
    LOCAL_LDLIBS     += -llog -ldl

    LOCAL_MODULE     := IDNumberOCR

    include $(BUILD_SHARED_LIBRARY)

编辑Application.mk

    APP_STL := c++_static
    APP_CPPFLAGS := -frtti -fexceptions
    APP_ABI := arm64-v8a armeabi-v7a
    APP_PLATFORM := android-8