from socket import * 
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)

while True:
    client, addr = s.accept()
    while True:
        data = client.recv(1024)
        if not data:
            break
        number1, operator, number2 =data.decode().split()
        
        if operator == '+':
            ans = int(number1) + int(number2)
        elif operator == '-':
            ans = int(number1) - int(number2)
        elif operator == '*':
            ans = int(number1) * int(number2)
        elif operator == '/':
            ans = int(number1) / int(number2)
        client.send(str(ans).encode())
        
    client.close()            