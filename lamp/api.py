from typing import Callable
from lamp import device


# 设置回调函数，当电灯打开、关闭、上线、离线时会调用回调函数
# 并传入事件如 'on', 'off', 'online', 'offline'
def set_callback(func: Callable[[str], None]):
    device.set_message_callback(func)


# 设置电灯状态 True 为开灯，False 为关灯
def set_status(value: bool):
    commands = {'commands': [{'code': 'switch_on', 'value': value}]}
    device.send_commands(commands)


# 开灯
def on():
    set_status(True)


# 关灯
def off():
    set_status(False)


# 查询电灯状态 True 为开灯，False 为关灯
def status():
    result = device.dev_status()
    return result['result'][0]['value']


# 查询电灯是否在线 True 为在线，False 为离线
def is_online():
    result = device.dev_info()
    return result['result']['online']
