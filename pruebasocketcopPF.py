import sim, time
#import socket, pickle, time

def conectar(port):
    sim.simxFinish(-1)
    dirCliente = sim.simxStart("127.0.0.1", port, True, True, 2000, 5)
    if dirCliente ==0:
        print("Conexion OK ", port)
    else:
        print("Conexion Fallida ", port)
    return dirCliente

cliente= conectar(19999)

ret, m1 = sim.simxGetObjectHandle(cliente, "m1", sim.simx_opmode_blocking)
i=0

while True:
    sim.simxSetJointTargetPosition(cliente, m1, i, sim.simx_opmode_oneshot)
    ret, p1= sim.simxGetJointPosition(cliente, m1, sim.simx_opmode_blocking)
    print(p1)
    i=i+0.1
    time.sleep(1)
