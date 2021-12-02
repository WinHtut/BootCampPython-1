import socket

class Cleint:
    def __init__(self,ClientMessage):
        self.target_host ='localhost'
        self.target_port = 9998
        self.ClientMessage = bytes(ClientMessage,'utf-8')

    def runCleint(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_host,self.target_port))

        client.send(self.ClientMessage)
        dataFromServer = client.recv(1024)
        DecodedData  = dataFromServer.decode('utf-8')
        print("Data Received From Server ",DecodedData)

        client.close()

if __name__ == "__main__":
    while True:
        clientMessage = input("Enter message to send:>")
        ClientConnector = Cleint(clientMessage)
        ClientConnector.runCleint()