import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("[*] connected", self.client_address[0])
        s = self.request
        try:
            while True:
                print('[-] Waiting for response...')
                print((s.recv(1024)).decode('utf-8'))
                OkMsg = "OK!"
                s.send(OkMsg.encode('utf-8'))
        except:
            s.close()
            print("[!] disconnected")

def main():
    host = "127.0.0.1"
    port = 33344

    server = socketserver.TCPServer((host, port),MyTCPHandler)

    print("[*] server start")

    server.serve_forever()


if __name__ == '__main__':
    try:
        main()
    except:
        print("[*] server stop")
