#Servidor TCP
import socket
# Endereco IP do Servidor
HOST = '192.168.15.63'
# Porta que o Servidor vai escutar
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Conecqtado por ', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(msg)
    print ('Finalizando conexao do cliente', cliente)
    con.close()
