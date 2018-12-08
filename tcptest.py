# tcp 通信程序
import socket

words = {'how are you': 'Fine,thank you'}
HOST = ''
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定socket
s.bind((HOST, PORT))
# 开始监听
s.listen(1)  # 限定监听数为1
print('正在监听的端口：', PORT)

conn, addr = s.accept()
print("连接的地址：", addr)
while True:
    data = conn.recv()
    data = data.decode('utf-8')
    if not data:
        break
    print('接受的信息：', data)
    conn.sendall(words.get(data, 'Nothing').encode('utf-8'))

conn.close()  # 关闭连接
s.close()  # 关闭socket

# 客服端
import socket
import sys

HOST = '127.0.0.1'
PORT = '8080'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except:
    print("未找到服务器")
    sys.exit()
while True:
    c = input('>>>')
    c.sendall(c.encode('utf-8'))
    data = s.recv(1024)
    data = data.decode('utf-8')
    print("收到的数据：", data)
    if c.lower() == 'bye':
        break
s.close()
