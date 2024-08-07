import socket, pickle, time

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.bind(("",12345))
s.listen(1)

sc, addr= s.accept()
while True:
    datosrec= sc.recv(1024)
    n = pickle.loads(datosrec)
    time.sleep(0.01)
    print(n)
    if n[0]==1:
        break
    sc.close()
    s.close()

        
