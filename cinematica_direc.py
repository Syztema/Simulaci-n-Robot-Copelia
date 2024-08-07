
import sympy as sm
from sympy import sin, cos


def cd_pos(q, r):
    d1=183
    a2=30
    a3=30
    d4=221.5
    d6=23.7

    cd = sm.Matrix(
        [cos(q[0]) * (a3 * cos(q[1] + q[2]) + a2 * cos(q[1])) - d1 * sin(q[1] + q[2]) * cos(q[0]) + d6 * r[2],
         sin(q[0]) * (a3 * cos(q[1] + q[2]) + a2 * cos(q[1])) - d1 * sin(q[1] + q[2]) * sin(q[0]) + d6 * r[5],
         d1 + d1 * cos(q[1] + q[2]) + a3 * sin(q[1] + q[2]) + a2 * sin(q[1]) + d6 * r[8]])
    return cd


def rot_x(ax):
    rtx = sm.Matrix([[1, 0, 0],
                     [0, cos(ax), -sin(ax)],
                     [0, sin(ax), cos(ax)]])
    return rtx.evalf(5)


def rot_y(ay):
    rty = sm.Matrix([[cos(ay), 0, sin(ay)],
                     [0, 1, 0],
                     [-sin(ay), 0, cos(ay)]])
    return rty.evalf(5)


def rot_z(az):
    rtz = sm.Matrix([[cos(az), -sin(az), 0],
                     [sin(az), cos(az), 0],
                     [0, 0, 1]])
    return rtz.evalf(5)
