
# json文件读写

参考：[6.2 读写JSON数据](https://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html)

## 导入

```
import json
```

## 示例

读取文件

```
import json

if __name__ == '__main__':
    ...
    ...
    with open(file_path, 'w') as f:
        json_data = json.load(f)

```

写入文件

```
import json

if __name__ == '__main__':
    ...
    ...
    with open(file_path, 'w') as f:
        json.dump(json_data, f)
```