import socket
import ssl

key_file = '' # 服务器的私钥
cert_file = '' # 发送给客户端的证书

def echo_client(s):
    while True:
        data = s.recv(8192)
        if not data:
            break
        s.send(data)
    s.close()
    print('connection closed')

def echo_server(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(address)
    s.listen(5)

    s_ssl = ssl.wrap_socket(s,
                            keyfile=key_file,
                            certfile=cert_file,
                            server_side=True)
    while True:
        try:
            sock, address = s_ssl.accept()
            print('connection from', address, sock)
            echo_client(sock)
        except Exception as err:
            print(err)

def ssl_client(address):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_c = ssl.wrap_socket(s,
                            cert_reqs=ssl.CERT_REQUIRED,
                            ca_certs='server_cert.pem')
    ssl_c.connect(address)
    ssl_c.send(b'hello ssl socket')
    print(ssl_c.recv(8192)
            
if __name__ == '__main__':
    echo_server(('', 8080))
