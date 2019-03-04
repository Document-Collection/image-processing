
# [JNI]数据类型转换

参考:[JNI Types and Data Structures](https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/types.html)

JNI实现了Java类型到C类型的映射

## 原始类型

Java原始类型和C类型的映射以及所占位数如下

    Java Type   Native Type   Description        描述
    boolean     jboolean      unsigned 8 bits    无符号8位
    byte                     signed 8 bits       有符号8位
    char        jchar         unsigned 16 bits   无符号16位
    short       jshort        signed 16 bits     16位
    int         jint          signed 32 bits     32位
    long        jlong         signed 64 bits     64位
    float       jfloat        32 bits            32位
    double      jdouble       64 bits            64位
    void        void          N/A

与此同时,JNI还设置了两个宏定义以及一个类型定义

    #define JNI_FALSE  0 
    #define JNI_TRUE   1 

    typedef jint jsize; 

与此相对应的是C语言的原始类型,以及它们所占位数如下

    C Type         Description                描述
    unsigned char  unsigned 8 bits            无符号8位
    char           8 bits                     8位
    unsigned short unsigned 16 bits           无符号16位
    short          16 bits                    16位
    unsigned int   unsigned 16 bits or more   无符号16位(至少16位)
    int            16 bits or more            16位(至少16位)
    unsigned long  unsigned 32 bits           无符号32位
    long           32 bits                    32位
    float          32 bits                    32位
    double         64 bits                    64位
    long double    128 bits                   128位

转换如下所示:

