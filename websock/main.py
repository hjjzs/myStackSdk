# coding=utf-8
import json
import time
from websocket import create_connection


class websocket:
    def __init__(self, address):
        self.ws = create_connection(address)

    def send(self, params):
        print("Sending ...")
        self.ws.send(json.dumps(params))
        print("Reeiving...")
        result = self.ws.recv()
        print("Received '{}'".format(result))

    def quit(self):
        self.ws.close()


t = str(time.time() * 1000).split(".")[0]
address = "ws://39.106.85.158:8090/haiyou/device"

params1 = {
    "version": 1,
    "msgNo": t,
    "machNo": "U040119110001",
    "cmd": 1,
    "time": t
}

params2 = {
    "version": 1,
    "msgNo": t,
    "machNo": "U040119110001",
    "cmd": 7,
    "time": t,
    "data": {
        "userId": 8,
        "companyType": 3,
        "before": 0,
        "after": 100,
        "openTime": t,
        "closeTime": t
    }
}

# 初始化
webso = websocket(address)

# 发送数据
webso.send(params1)
webso.send(params2)

# 断开连接
webso.quit()