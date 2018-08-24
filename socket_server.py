import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("[*] connected", self.client_address[0])
        s = self.request
        try:
            while True:
                print('[-] Waiting for response...')
                data = (s.recv(1024)).decode('utf-8')
                print(data)
                OkMsg = "OK!"
                s.send(OkMsg.encode('utf-8'))
                scoreboard(data)    
        except:
            s.close()
            print("[!] disconnected")

def scoreboard(score):
    f = open("scoreboard.txt", "a")
    f.write("\n"+str(score))
    f.close


def main():
    host = ""
    port = 8080

    server = socketserver.TCPServer((host, port),MyTCPHandler)

    print("[*] server start")

    server.serve_forever()


if __name__ == '__main__':
    try:
        main()
    except:
        print("[*] server stop")
