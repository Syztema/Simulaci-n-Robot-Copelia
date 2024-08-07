import socket, pickle

def init_socket(ip, puerto):
    c=0
    s = socket.socket()
    try:
        s.connect((ip,puerto))
    except:
        print("No se pudo conectar al socket")
        c=1
    return s, c

def send_data(s, datos):
    mensaje=pickle.dumps(datos)
    try:
        s.send(mensaje)
    except:
        pass
