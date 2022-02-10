import socket
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)
print(f'el nombre de tu pc es : {hostname}')
print(f'la direccion de tu ip es : {ip}')