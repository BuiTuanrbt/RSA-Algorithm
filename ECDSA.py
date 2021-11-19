from ctypes import WINFUNCTYPE
import random as rd
import math


def square_multi(m,n):
    if n== 0:
        return 1
    if n % 2==0:
        return square_multi(m,n/2)**2
    else:
        return (square_multi(m,math.floor(n/2))**2)*m

def is_prime(p):
    is_prime= True
    i=1
    while i <=  math.ceil(math.sqrt(p)):
        i+=1
        if p%i==0:
            is_prime=False
    return is_prime

def find_all_point(a, b, p):
    if not(is_prime(p)):
        raise ValueError("p must be prime")
    elliptic_curve=[]
    for x in range(1,p):
        modulo_x = (square_multi(x,3) + a* x+b) % p
        for y in range(1,p):
            modulo_y = (square_multi(y, 2))%p
            if modulo_x == modulo_y:
                elliptic_curve.append([x, y])
 
    return elliptic_curve


def add_point(point_p,point_q):
    point_r=[0, 0]
    m = (point_p[1] - point_q[1]) / (point_p[0] - point_q[0])

    point_r[0] = m**2 - point_p[0] - point_q[0]
    point_r[1] = m*(point_p[0] - point_r[0]) - point_p[1]
    return point_r

def mult_point(point_p, point_q):
	point_r = [0, 0]
	m = (point_p[1] - point_q[1]) / (point_p[0] - point_q[0])

	point_r[0] = m**2 - 2 * point_p[0]
	point_r[1] = m*(point_p[0] - point_r[0]) - point_p[1]
	return point_r

def public_key(G,dA):
    Qa = [0, 0]
    i = 1
    while i < dA:
        Qa =  add_point(Qa,G)
        i += 1

    return Qa


def sign(m, G, dA, p):

    pass
# elliptic_curve = find_all_point(4, 8, 19)
# print(elliptic_curve[5])
# print(public_key(elliptic_curve[5], 37)[0].encode('ASCII'))