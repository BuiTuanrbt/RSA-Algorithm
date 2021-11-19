from os import path


def GCD(a,b):
	if b == 0:
		return a
	return GCD(b,a%b)

# ax +by =UCLN(a,b)=d
def GCD_extended(a, b):
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, b
	while v3 != 0:
		q = u3//v3
		t1, t2, t3 = u1 - q*v1, u2 - q*v2, u3 %v3
		u1, u2, u3 = v1, v2, v3
		v1, v2, v3 = t1, t2, t3
	return u1, u2, u3
def md_ex(base, power, module):
	a =1
	while power:
		power, d = power//2, power %2
		if d:
			a = a *base%module
		base =  base *base % module
	return a