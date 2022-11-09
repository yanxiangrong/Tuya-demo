# 涂鸦智能灯控制库

> 作者：严相荣  
> 最后修改日期：2022年11月9日

![PyPI - Python Version](https://img.shields.io/badge/python-3.6%7C3.7%7C3.8%7C3.9%7C3.10-blue)

&emsp;&emsp;这是一个控制智能灯的库，实际上控制的是 WIFI 插座。本程序可以接入涂鸦物联网云平台，来实现对插座的开电和关电的控制，以及监测插座的状态（开或关）。

## 快速开始

1. 设置 PyPI 镜像源，可以大幅提高 pip 下载速度，该步骤为可选的。
    ```shell
    python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    ```
2. 安装依赖库
   ```shell
   python setup.py
   ```
   或者
   ```shell
   pip install -r requirements.txt
   ```
3. 下面是一个简单的例子
   ```python
   import time
   import lamp
   
   
   # 当电灯状态改变时就会调用这个函数
   def status_callback(status):
       if status == 'on':
           print('[消息] 电灯已打开')
       elif status == 'off':
           print('[消息] 电灯已关闭')
       elif status == 'online':
           print('[消息] 电灯已上线')
       elif status == 'offline':
           print('[消息] 电灯已离线')
   
   
   def main():
       # 设置回调函数，当电灯打开、关闭、上线、离线时会调用回调函数
       # 并传入事件如 'on', 'off', 'online', 'offline'
       lamp.set_callback(status_callback)
   
        # 查询电灯是否在线 True 为在线，False 为离线
       if lamp.is_online():
           print('电灯是在线的')
       else:
           print('电灯是离线的')
   
       # 查询电灯状态 True 为开灯，False 为关灯
       if lamp.status():
           print('电灯是开着的')
       else:
           print('电灯是关着的')
   
       for i in range(3):
           # 开灯
           lamp.on()
   
           time.sleep(3)
   
           # 关灯
           lamp.off()
   
           time.sleep(3)
   
   
   if __name__ == '__main__':
       main()

   ```

## API 参考

`on()`, `off()`, `status()`, `is_online()`, `set_callback()` 方法在上文已有说明，这里不再赘述。

* `set_status(value)`  
  设置电灯状态 True 为开灯，False 为关灯.

## 移植

下面介绍如何将本库移植到自己的项目

1. 将 `lamp` 文件夹复制到自己的项目中
2. 安装依赖库（上文已有介绍）
3. 在项目中用 `import lamp` 导入即可
