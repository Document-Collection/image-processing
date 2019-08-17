
# [c++11]queue

`c++`提供了队列的实现：[queue](http://www.cplusplus.com/reference/queue/queue/)

## 创建队列

引入头文件`queue`，创建时指定数据类型：

```
#include <queue>

queue<int> q;
```

## 队列功能

`queue`提供了如下常用功能实现：

* empty()：判断队列是否问空，为空返回`true`，不为空返回`false`
* size()：返回队列大小
* front()：返回队头（第一个出队）数据
* back()：返回队尾（第一个入队）数据
* push(value_type&& __x)：添加数据到队尾
* pop()：移除队头数据。注意，返回值为空

`c++11`还提供了不太常用的[swap](http://www.cplusplus.com/reference/queue/queue/swap/)功能，就是交换两个队列值

## 实现

```
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    // 队列大小
    cout << q.size() << endl;
    // 队列是否为空
    cout << q.empty() << endl;

    q.push(3);
    q.push(4);
    q.push(5);

    // 队头元素
    cout << q.front() << endl;
    // 队尾元素
    cout << q.back() << endl;

    queue<int> s;
    s.push(3232);

    q.swap(s);
    cout << q.size() << endl;
    cout << q.empty() << endl;
}
```