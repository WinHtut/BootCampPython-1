import socket
import threading
import FetchData

class TCPserver():
    def __init__(self):
        self.server_ip="localhost"
        self.server_port=9998

    def main(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((self.server_ip,self.server_port))
        server.listen(6)
        print(f'Server listen on {self.server_ip} : Port:{self.server_port}')

        while True:
            cleint , address = server.accept()
            print(f'[+] Accepted conneciton from {address[0]} : {address[1]}')
            cleint_handler = threading.Thread(target=self.handle_client , args=(cleint,))
            cleint_handler.start()


    def handle_client(self,client_socket):
        with client_socket as sock:
            request  = sock.recv(1024)
            toFindInDatabase = request.decode()
            print('[*] Received Data From Cleint:',toFindInDatabase)
            receivedFromDatabase = self.toFind(toFindInDatabase)

            toSend=bytes(receivedFromDatabase,'utf-8')
            sock.send(toSend)

    def toFind(self,toFindInDatabase):
        db =FetchData.DatabaseClass(toFindInDatabase)
        DBdata=db.databaseMethod()
        return DBdata

if __name__ == "__main__":
    while True:
        server =TCPserver()
        server.main()