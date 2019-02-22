
# [Ubuntu 16.04][Anaconda3][Python3.7]OpenCV-3.4安装


    # 进入opencv源码路径，新建用于存储配置文件的build文件夹和用于存储库文件的install文件夹
    $ cd opencv
    $ mkdir build
    $ mkdir install

    # 进入build文件夹，利用cmake生产makefile，然后进行编译和安装
    $ cd build
    $ cmake -D CMAKE_BUILD_TYPE=RELEASE \  
        -D CMAKE_INSTALL_PREFIX=../install \  
        -D BUILD_DOCS=ON \
        -D BUILD_EXAMPLES=ON \
        -D BUILD_opencv_python2=OFF \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D OPENCV_PYTHON3_VERSION=ON \
        -D PYTHON3_EXECUTABLE=<anaconda_work_dir>/envs/<environment>/bin/python \  
        -D PYTHON3_LIBRARY=<anaconda_work_dir>/envs/<environment>/lib/python3.7 \  
        -D PYTHON3_INCLUDE_DIR=<anaconda_work_dir>/envs/<environment>/include/python3.7m \  
        -D PYTHON3_NUMPY_INCLUDE_DIRS=<anaconda_work_dir>/envs/<environment>/lib/python3.7/site-packages/numpy/core/include
        ..

    $ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=../install -D BUILD_DOCS=ON -D BUILD_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D PYTHON3_EXECUTABLE=/home/zj/software/anaconda/anaconda3/envs/py37/bin/python -D PYTHON3_LIBRARY=/home/zj/software/anaconda/anaconda3/envs/py37/lib/python3.7 -D PYTHON3_INCLUDE_DIR=/home/zj/software/anaconda/anaconda3/envs/py37/include/python3.7m -D PYTHON3_NUMPY_INCLUDE_DIRS=/home/zj/software/anaconda/anaconda3/envs/py37/lib/python3.7/site-packages/numpy/core/include ..
    ...
    ...
    -- General configuration for OpenCV 3.4.5-dev =====================================
    --   Version control:               3.4.5-195-g0e70363
    -- 
    --   Platform:
    --     Timestamp:                   2019-02-22T06:59:41Z
    --     Host:                        Linux 4.15.0-43-generic x86_64
    --     CMake:                       3.5.1
    --     CMake generator:             Unix Makefiles
    --     CMake build tool:            /usr/bin/make
    --     Configuration:               RELEASE
    -- 
    --   CPU/HW features:
    --     Baseline:                    SSE SSE2 SSE3
    --       requested:                 SSE3
    --     Dispatched code generation:  SSE4_1 SSE4_2 FP16 AVX AVX2 AVX512_SKX
    --       requested:                 SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
    --       SSE4_1 (6 files):          + SSSE3 SSE4_1
    --       SSE4_2 (2 files):          + SSSE3 SSE4_1 POPCNT SSE4_2
    --       FP16 (1 files):            + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 AVX
    --       AVX (6 files):             + SSSE3 SSE4_1 POPCNT SSE4_2 AVX
    --       AVX2 (18 files):           + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2
    --       AVX512_SKX (2 files):      + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2 AVX_512F AVX512_SKX
    -- 
    --   C/C++:
    --     Built as dynamic libs?:      YES
    --     C++ Compiler:                /usr/bin/c++  (ver 5.4.0)
    --     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
    --     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
    --     C Compiler:                  /usr/bin/cc
    --     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-narrowing -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
    --     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-narrowing -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
    --     Linker flags (Release):      
    --     Linker flags (Debug):        
    --     ccache:                      NO
    --     Precompiled headers:         YES
    --     Extra dependencies:          dl m pthread rt
    --     3rdparty dependencies:
    -- 
    --   OpenCV modules:
    --     To be built:                 calib3d core dnn features2d flann highgui imgcodecs imgproc java_bindings_generator ml objdetect photo python2 python3 python_bindings_generator shape stitching superres ts video videoio videostab
    --     Disabled:                    world
    --     Disabled by dependency:      -
    --     Unavailable:                 cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev java js viz
    --     Applications:                tests perf_tests examples apps
    --     Documentation:               NO
    --     Non-free algorithms:         NO
    -- 
    --   GUI: 
    --     GTK+:                        YES (ver 3.18.9)
    --       GThread :                  YES (ver 2.48.2)
    --       GtkGlExt:                  NO
    --     VTK support:                 NO
    -- 
    --   Media I/O: 
    --     ZLib:                        /home/zj/software/anaconda/anaconda3/lib/libz.so (ver 1.2.11)
    --     JPEG:                        /home/zj/software/anaconda/anaconda3/lib/libjpeg.so (ver 90)
    --     WEBP:                        build (ver encoder: 0x020e)
    --     PNG:                         /home/zj/software/anaconda/anaconda3/lib/libpng.so (ver 1.6.35)
    --     TIFF:                        /home/zj/software/anaconda/anaconda3/lib/libtiff.so (ver 42 / 4.0.9)
    --     JPEG 2000:                   /usr/lib/x86_64-linux-gnu/libjasper.so (ver 1.900.1)
    --     OpenEXR:                     build (ver 1.7.1)
    --     HDR:                         YES
    --     SUNRASTER:                   YES
    --     PXM:                         YES
    -- 
    --   Video I/O:
    --     DC1394:                      YES (ver 2.2.4)
    --     FFMPEG:                      YES
    --       avcodec:                   YES (ver 56.60.100)
    --       avformat:                  YES (ver 56.40.101)
    --       avutil:                    YES (ver 54.31.100)
    --       swscale:                   YES (ver 3.1.101)
    --       avresample:                NO
    --     GStreamer:                   NO
    --     libv4l/libv4l2:              NO
    --     v4l/v4l2:                    linux/videodev2.h
    -- 
    --   Parallel framework:            pthreads
    -- 
    --   Trace:                         YES (with Intel ITT)
    -- 
    --   Other third-party libraries:
    --     Intel IPP:                   2019.0.0 Gold [2019.0.0]
    --            at:                   /home/zj/opencv/opencv/build/3rdparty/ippicv/ippicv_lnx/icv
    --     Intel IPP IW:                sources (2019.0.0)
    --               at:                /home/zj/opencv/opencv/build/3rdparty/ippicv/ippicv_lnx/iw
    --     Lapack:                      NO
    --     Eigen:                       NO
    --     Custom HAL:                  NO
    --     Protobuf:                    build (3.5.1)
    -- 
    --   OpenCL:                        YES (no extra features)
    --     Include path:                /home/zj/opencv/opencv/3rdparty/include/opencl/1.2
    --     Link libraries:              Dynamic load
    -- 
    --   Python 2:
    --     Interpreter:                 /usr/bin/python2.7 (ver 2.7.12)
    --     Libraries:                   /usr/lib/x86_64-linux-gnu/libpython2.7.so (ver 2.7.12)
    --     numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include (ver 1.11.0)
    --     install path:                lib/python2.7/dist-packages/cv2/python-2.7
    -- 
    --   Python 3:
    --     Interpreter:                 /home/zj/software/anaconda/anaconda3/envs/py37/bin/python (ver 3.7.2)
    --     Libraries:                   /home/zj/software/anaconda/anaconda3/envs/py37/lib/python3.7 (ver 3.7.2)
    --     numpy:                       /home/zj/software/anaconda/anaconda3/envs/py37/lib/python3.7/site-packages/numpy/core/include (ver 1.15.4)
    --     install path:                lib/python3.7/site-packages/cv2/python-3.7
    -- 
    --   Python (for build):            /usr/bin/python2.7
    --     Pylint:                      /home/zj/software/anaconda/anaconda3/bin/pylint (ver: 3.7.1, checks: 163)
    -- 
    --   Java:                          
    --     ant:                         NO
    --     JNI:                         NO
    --     Java wrappers:               NO
    --     Java tests:                  NO
    -- 
    --   Install to:                    /home/zj/opencv/opencv/install
    -- -----------------------------------------------------------------
    -- 
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/zj/opencv/opencv/build