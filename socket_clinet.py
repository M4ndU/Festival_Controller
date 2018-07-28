import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 33344

s.connect((host, port))
print( '[*] Connected to', host)

try:
    while True:
        SendMsg = input("Enter something for the server: ")
        s.send(SendMsg.encode('utf-8'))
        print ('[-] Waiting for response...')
        print ((s.recv(1024)).decode('utf-8'))
except:
    s.close()
    print("\n[!] disconnected")
