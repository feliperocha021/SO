import socket
import threading
from datetime import datetime

def funcao(client):
    while True:
        data_payload = 2048 
        print ("Esperando mensagem do cliente")
        data = client.recv(data_payload)
        if data:
            if data.decode() == 'data':
                client.sendall(datetime.today().strftime('%Y-%m-%d').encode())
            elif data.decode() == 'hora':
                client.sendall(datetime.today().strftime('%H:%M:%S').encode())
            elif data.decode() == 'data-hora':
                client.sendall(datetime.today().strftime('%Y-%m-%d / %H:%M:%S').encode())
            elif data.decode() == '/sair':
                client.sendall('/sair'.encode())
                break
            else:
                client.sendall('Mensagem inválida!'.encode())
    client.close()

def server(host = '10.0.84.187', port=8082):
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = (host, port)
    print ("Iniciando servidor na porta %s %s" % server_address)
    sock.bind(server_address)
    
    sock.listen(5)
    
    while True:
        client, address = sock.accept()
        t1 = threading.Thread(target=funcao, args=(client,))
        t1.start()
        
server()