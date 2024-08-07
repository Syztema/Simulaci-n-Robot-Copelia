from cinematica_direc import *
from gamepad import *
from sympy import pi
import sympy as sm
from cliente_socket import *
import time
from cinematica_inversa import *
from CopeAlone import *


def main():
    print("Iniciando el programa")
    control=init_gamepad()
    #Inicializado los Q
    q = sm.Matrix([1.57, 1.57, 0, 0, 0, 0]).evalf(5)
    datos=[0, 0, 0, 0, 0, 0, 0]
    j = jac()
    Mort=sm.Matrix([[1,0,0],
                    [0, 1,0],
                    [0,0,1]])

    if control !=0:
        sock, connect= init_socket("192.168.245.147",12345)
        #connect=0
        if connect!=1:
            #cliente = conectar(19999)

            while True:
                dPosC,stop, ori =control_read(control)
                if stop==1:
                    datos[0]=1
                    send_data(sock,datos)
                    break
                cd_ant =cd_pos(q, Mort)
                Mort=rot_x(ori)*rot_y(ori)*rot_z(ori)
                cd_nueva = cd_pos(q, Mort)
                dPosD=(cd_ant-cd_nueva)

                dPos=dPosC+dPosD

                datos[4],datos[5],datos[6]=ci_ori(Mort)
                q[3], q[4], q[5] =ci_ori(Mort)
                posd=cd_pos(q, Mort)+dPos
                q[0], q[1], q[2]=ci_mn(j, q, posd, Mort)
                datos[1]=q[0]
                datos[2]=q[1]
                datos[3]=q[2]
                print(q)#Prueba 1 %pi.evalf(5)
                #print(Mort)#Prueba 2


                datos_cop(datos, cliente)

                send_data(sock, datos)
                #print(posd)
                time.sleep(0.1)

        sock.close()

if __name__== "__main__":
    main()
