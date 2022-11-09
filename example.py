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
