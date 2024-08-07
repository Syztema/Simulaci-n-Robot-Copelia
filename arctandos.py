from sympy import atan2, pi

def atands(num, den):
    if den>0:
        ang=atan2(num,den).evalf(5)
    elif den<0 and num>=0:
        ang=(atan2(num,den)+pi).evalf(5)
    elif den<0 and num<0:
        ang=(atan2(num,den)-pi).evalf(5)
    elif den==0 and num>0:
        ang=(pi/2).evalf(5)
    elif den==0 and num<0:
        ang=(-pi/2).evalf(5)
    else:
        ang=0
    return ang
#print(atands(1,2))