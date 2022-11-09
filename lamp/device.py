import json
import logging
from typing import Callable
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER, TuyaOpenPulsar, TuyaCloudPulsarTopic
from lamp.env import ACCESS_ID, ACCESS_KEY, API_ENDPOINT, DEVICE_ID, MQ_ENDPOINT

# 设置日志等级
TUYA_LOGGER.setLevel(logging.INFO)


def message_handler(message):
    message = json.loads(message)
    result = ''
    if message['devId'] != DEVICE_ID:
        return
    try:
        if message['status'][0]['value']:
            result = 'on'
        else:
            result = 'off'
    except KeyError:
        try:
            result = message['bizData']
        except KeyError:
            pass

    callbackFunc(result)


# 初始化 openapi 和 连接
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)

# 初始化消息队列
open_pulsar = TuyaOpenPulsar(ACCESS_ID, ACCESS_KEY, MQ_ENDPOINT, TuyaCloudPulsarTopic.PROD)
# Add Message Queue listener
open_pulsar.add_message_listener(message_handler)
open_pulsar.daemon = True

isOpenPulsarStart = False
callbackFunc: Callable[[str], None]


# 连接涂鸦 Iot 平台
def connect():
    result = openapi.connect()
    if not result["success"]:
        TUYA_LOGGER.error(result['msg'])
        TUYA_LOGGER.error("连接涂鸦 Iot 平台失败")


def set_message_callback(func: Callable[[str], None]):
    global isOpenPulsarStart, callbackFunc
    callbackFunc = func

    if not isOpenPulsarStart:
        # Start Message Queue
        open_pulsar.start()
        isOpenPulsarStart = True


# 查询设备详情
def dev_info():
    res = openapi.get("/v1.0/iot-03/devices/{}".format(DEVICE_ID))
    if not res["success"]:
        TUYA_LOGGER.error(res['msg'])
        return None
    return res


# 查询设备指令集
def div_fun():
    res = openapi.get("/v1.0/iot-03/devices/{}/functions".format(DEVICE_ID))
    if not res["success"]:
        TUYA_LOGGER.error(res['msg'])
        return None
    return res


# 下发指令
def send_commands(commands):
    res = openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)
    if not res["success"]:
        TUYA_LOGGER.error(res['msg'])
        return None
    return res


# 查询设备状态
def dev_status():
    res = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))
    if not res["success"]:
        TUYA_LOGGER.error(res['msg'])
        return None
    return res
