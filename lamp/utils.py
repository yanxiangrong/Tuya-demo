from lamp import device


# 打印设备详情
def print_dev_info():
    info = device.dev_info()['result']
    print(f"{info['model']} {info['name']}  Online: {info['online']}")
