# 网络嗅探程序
import socket
import threading
import time

active_degree = dict()
flag = 1


def main():
    global active_degree
    global flag
    # 公共网路接口
    HOST = socket.gethostbyname(socket.gethostname())
    # 创建一个原生socket接口，并绑定
    sk = socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sk.bind((HOST, 0))
    # 包括ip头
    sk.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # 接收所有的包
    sk.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    # 接受单个包
    while flag:
        c = sk.recvform(65535)
        host = c[1][0]
        active_degree[host] = active_degree.get(host, 0) + 1
        if c[1][0] != '10.2.1.8':  # 当前ip
            print(c)

    sk.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    sk.close()


t = threading.Thread(target=main)
t.start()
time.sleep(60)
flag = 0
t.join()
for item in active_degree.items():
    print(item)
