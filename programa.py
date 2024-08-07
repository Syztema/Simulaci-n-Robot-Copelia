import sim
import socket, pickle, time

def conectar(port):
    sim.simxFinish(-1)
    dirCliente = sim.simxStart("10.0.35.69",port,True,True,2000,5)
    if dirCliente == 0:
        print ("Conexion ok",port)
    else:
        print("Conexion Fallida",port)
    return dirCliente
cliente = conectar(19999)

ret, mo1= sim.simxGetObjectHandle(cliente,"m1",sim.simx_opmode_blocking)
ret, mo2= sim.simxGetObjectHandle(cliente,"m2",sim.simx_opmode_blocking) #antes del while 1

i=0
j=0

while True:
    sim.simxSetJointTargetPosition(cliente,mo1,i,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(cliente,mo2,j,sim.simx_opmode_oneshot)
    ret,p1 = sim.simxGetJointPosition(cliente,mo1,sim.simx_opmode_blocking)

    print(p1)
    i=i+0.1
    j=j+0.1
