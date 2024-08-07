
import sympy as sm
from arctandos import *
from math import acos
from sympy import sin, cos
from cinematica_direc import *


def ci_ori(r):
    t4 = atands(r[5], r[2])
    t5 = acos(r[8])
    t6 = atands(r[7], r[6])
    return t4, t5, t6


def jac():
    t1, t2, t3, r3, r6, r9 = sm.symbols("t1 t2 t3 r3 r6 r9 ")
    d1=183
    a2=30
    a3=30
    d4=221.5
    d6=23.7
    cd = sm.Matrix([cos(t1) * (a3 * cos(t2 + t3) + a2 * cos(t2)) - d1 * sin(t2 + t3) * cos(t1) + d6 * r3,
                    sin(t1) * (a3 * cos(t2 + t3) + a2 * cos(t2)) - d1 * sin(t2 + t3) * sin(t1) + d6 * r6,
                    d1 + d1 * cos(t2 + t3) + a3 * sin(t2 + t3) + a2 * sin(t2) + d6 * r9])

    q = sm.Matrix([t1, t2, t3])
    j = cd.jacobian(q)
    return j


def ci_mn(j, q, pd, r):
    #cd_pos(q, r)  #cinematica directa
    e = 1e-3 #dimensiones de su robot
    # error de posicion necesitamos la cinemtica directa
    epos = (pd - cd_pos(q, r))
    cont = 0
    qn = sm.Matrix([q[0], q[1], q[2]]).evalf(5)
    #print(qn)
    while True:
        if (abs(epos[0]) < e and abs(epos[1]) < e and abs(epos[2]) < e) or cont > 30:
            if cont < 30:
                q = qn

            break
        jac = j.subs([("t1", qn[0]),
                      ("t2", qn[1]),
                      ("t3", qn[2]),
                      ("r3", r[2]),
                      ("r6", r[5]),
                      ("r9", r[8])]).evalf(5)

        jinv = jac.pinv().evalf(5)
        qn = (qn + jinv * epos).evalf(5)
        #print(qn)
        #print(cont)
        epos = (pd - (cd_pos(qn, r))).evalf(5)
        #print(epos)
        cont = cont + 1

    return q[0], q[1], q[2]







