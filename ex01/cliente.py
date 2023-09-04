import socket

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('10.0.84.187', 8082)
    print ("Conectando %s porta %s" % server_address)
    sock.connect(server_address)
    while True:
        try:
            message = input("Digite a mensagem a ser enviada: ")
            print ("Esperando resposta...")

            sock.sendall(message.encode('utf-8'))
            data = sock.recv(2048)
            print(data.decode())
            if data.decode() == "/sair":
                sock.close()
                break
        except Exception as e:
            print(e)
client()