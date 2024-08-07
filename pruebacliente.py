import socket, pickle, time

s = socket.socket()
s.connect(("192.168.76.111",12345))

datos = [0, -123.34, 6565, 78456]
cont=0
while True:
    mensaje=pickle.dumps(datos)
    print(mensaje)
    try:
        s.send(mensaje)
    except:
        pass
    cont=cont+1
    time.sleep(0.3)
    if cont>100:
        datos[0]=1
        try:
            mensaje=pickle.dumps(datos)
            s.send(mensaje)
            break
        except:
            break
       
s.close()
