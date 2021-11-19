import random
def md_ex(base, power, module):
    a =1
    while power:
        power, d = power//2, power %2
        if d:
            a = a *base%module
        base =  base *base % module
    return a
def fermat_test(n,k):
    if n >1:
        if n == 2 or n==3:
            return True
        if n % 2==0:
            return False
        for i in range(k):
            a = random.randint(1, n-1)
            if md_ex(a,n-1,n) !=1:
                return False
        return True
def miller_rabin(n, k):
    if n == 2 or n==3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = md_ex(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = md_ex(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime(n,k):
    if fermat_test(n,k) == True & miller_rabin(n,k)== True:
        return True
    else:
        return False
def GetPrime(b):
    p = random.getrandbits(b)
    p = p |(1 <<(b-1))
    p = p | 1
    while True:
        if fermat_test(p,20) & miller_rabin(p,20):
            break
        else:
            p+=2
    return p

p = GetPrime(1024)
q = GetPrime(1024)
f=open("prime1.txt","w")
f.write(str(p)+'\n')
f.write(str(q))