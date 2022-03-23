import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
sock.send("Jeonghyun Song".encode())
msg_stu = sock.recv(1024)
student_number = int.from_bytes(msg_stu, 'big')
print(student_number)
sock.close()