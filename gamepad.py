import pygame
import sympy as sm

def init_gamepad():
    pygame.init()
    jcount=pygame.joystick.get_count()
    control=0
    if jcount==0:
        print("No hay Control")
    else:
        control =pygame.joystick.Joystick(0)
        control.init()
    return control

mov=0
ori = 0
def control_read(control):
    pos=sm.Matrix([[0],
                   [0],
                   [0]])
    stop=0
    global mov
    global ori

    mode = 0
    for event in pygame.event.get():
        if event.type == 1539:
            if event.type == 1539:
                if event.button == 3:
                    if mov == 0:
                        pos[0, 0] = pos[0, 0] + 2
                        # print(pos)
                    else:
                        ori = ori + 2
                if event.button == 11:
                    if mov == 0:
                        pos[0, 0] = pos[0, 0] - 2
                    # print(pos)
                    else:
                        ori = ori - 2
                if event.button == 1:
                    if mov == 0:
                        pos[1, 0] = pos[1, 0] + 2
                    # print(pos)
                    else:
                        ori = ori + 2
                if event.button == 14:
                    if mov == 0:
                        pos[1, 0] = pos[1, 0] - 2
                    # print(pos)
                    else:
                        ori = ori - 2
                if event.button == 0:
                    if mov == 0:
                        pos[2, 0] = pos[2, 0] + 2
                    # print(pos)
                    else:
                        ori = ori + 2
                if event.button == 12:
                    if mov == 0:
                        pos[2, 0] = pos[2, 0] - 2
                    # print(pos)
                    else:
                        ori = ori - 2
                if event.button == 13:
                    mov = mov + 1
                    if mov > 1:
                        mov = 0
                if event.button == 15:
                    mode = mode + 1
                    if mode > 2:
                        mode = 0
                if event.button == 2:
                    stop = 1
                    print("PRESIONE BOTON STOP")

        #print(event)
    return pos, stop, ori

control = init_gamepad()
control_read(control)