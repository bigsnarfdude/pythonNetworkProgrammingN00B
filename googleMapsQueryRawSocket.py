import socket
sock = socket.socket()
sock.connect(('maps.google.com', 80))
sock.sendall(
'GET /maps/geo?q=1600+Amphitheatre+Parkway,+Mountain+View,+CA'
'&output=json&oe=utf8&sensor=false HTTP/1.1\r\n''Host: maps.google.com:80\r\n'
'User-Agent: search4.py\r\n'
'Connection: close\r\n'
'\r\n')
rawreply = sock.recv(4096)
print rawreply
