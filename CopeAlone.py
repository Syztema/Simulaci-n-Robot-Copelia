import sim, time
import socket, pickle, time



def conectar(port):
    sim.simxFinish(-1)
    dirCliente = sim.simxStart("127.0.0.1", port, True, True, 2000, 5)
    if dirCliente ==0:
        print("Conexion OK ", port)
    else:
        print("Conexion Fallida ", port)
    return dirCliente

def datos_cop(datos, cliente):

    cliente= conectar(19999)

    ret, m1 = sim.simxGetObjectHandle(cliente, "M1", sim.simx_opmode_blocking)
    ret2, m2 = sim.simxGetObjectHandle(cliente, "M2", sim.simx_opmode_blocking)
    ret3, m3 = sim.simxGetObjectHandle(cliente, "M3", sim.simx_opmode_blocking)
    ret4, m4 = sim.simxGetObjectHandle(cliente, "M4", sim.simx_opmode_blocking)
    ret5, m5 = sim.simxGetObjectHandle(cliente, "M5", sim.simx_opmode_blocking)
    ret6, m6 = sim.simxGetObjectHandle(cliente, "M6", sim.simx_opmode_blocking)

    sim.simxSetJointTargetPosition(cliente, m1, datos[1], sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(cliente, m2, datos[2], sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(cliente, m3, datos[3], sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(cliente, m4, datos[4], sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(cliente, m5, datos[5], sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(cliente, m6, datos[6], sim.simx_opmode_oneshot)



