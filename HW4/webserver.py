from socket import *
s = socket()
s.bind(('', 80))
s.listen(10)

while True :
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    data1, data2, data3 = req[0].split(' ')
    file = data2.strip("/")

    if file == 'index.html' :
        f = open('C:/vscode/HW4/index.html', 'r', encoding='utf-8')
        mimeType = 'text/html'
        content_data = f.read().encode('euc-kr') # 한글 텍스트 파일일 경우

    elif file == 'iot.png' :
        f = open('C:/vscode/HW4/iot.png', 'rb')
        mimeType = 'image/png'
        content_data = f.read()

    elif file == 'favicon.ico' :
        f = open('C:/vscode/HW4/favicon.ico', 'rb')
        mimeType = 'image/x-icon'
        content_data = f.read()

    else : # 해당 파일 존재하지 않을 경우
        send_msg = 'HTTP/1.1 404 Not Found\r\n' + '\r\n' + '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>' + '<BODY>Not Found</BODY></HTML>'
        c.send(send_msg.encode())
        break
    # HTTP 헤더 전송
    c.send(b'HTTP/1.1 200 OK\r\n')
    c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
    c.send('\r\n'.encode())

    # HTTP 바디 전송
    c.send(content_data)
    c.close()