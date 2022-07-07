#!/bin/python3
import socket
import os
import psutil
import time
import json

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

sock.bind(("192.168.1.100", 9999))

print("server is listening on port 9999")

def byteToGb(number):
    return round(number / 1024 ** 3, 2)

def getSystemStatus():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    data = {
        # you should understand how cpu loads are calculated
        "cpus": psutil.cpu_percent(percpu=True),
        "memory": {
            "total": byteToGb(memory.total),
            "free": byteToGb(memory.free),
            "used": byteToGb(memory.used),
            "percent": memory.percent
        },
        "disk": {
            "total": byteToGb(disk.total),
            "free": byteToGb(disk.free),
            "used": byteToGb(disk.used),
            "percent": disk.percent
        }
    }

    return json.dumps(data, indent=None, separators=(',', ':'))

while (True):
    pairs = sock.recvfrom(1024)
    msg = pairs[0].strip()
    addr = pairs[1]

    msgStr = msg.decode("utf-8")

    response = bytearray(getSystemStatus(), "ascii")
    sock.sendto(response, addr)