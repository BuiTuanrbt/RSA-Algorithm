from ctypes import FormatError
from hashlib import sha1
from mmap import ACCESS_DEFAULT
import random
import math
from ECDSA import is_prime
import Sha1
import time
import prime_test
start_time= time.time()

# def check_prime(n):
#     is_prime=True
#     i=1
#     while i<=math.ceil(math.sqrt(n)):
#         i+=1
#         if n % i==0:
#             is_prime=False
#     return is_prime

def choose_p(q): 
    p=0
    while p %2 ==0:
        r= random.random()
        k =  random.randrange(1,7)
        i= math.floor(r*(5**k))
        p=q*i+1
    while not(prime_test.is_prime(p,28)) or (p-1)%q !=0 :
        p +=2
        print(p)
    return p
def modular_exponentiation(m,e,n):
    e1=0
    c=1
    while e1<e:
        e1 +=1
        c=(m*c)%n
    return c
def choose_g(p, q):
    h = 1
    mod_g = 0
    g=0
    while g>p or mod_g !=1:

        h = random.randrange(2, p-1)
        print("h=",h)
        g =  modular_exponentiation(h,((p-1)/q),p)
        print("g=",g)
        print("p",p)
        mod_g = modular_exponentiation(g,q,p)
        print("mod_g=", mod_g)
    return g

def choose_x(q):
    x =  random.randrange(1,q)
    return x


def find_y(g ,x, p):
    y = modular_exponentiation(g,x,p)
    return y


def generate_key(q):
    if prime_test.is_prime(q,20):
        p = choose_p(q)
        print(p)
        g = choose_g(p,q)
        print("g",g)
        x = choose_x(q)
        y = find_y(g,x,p)
        # Public key ,Private key
        return (p,q,g,y),(p,q,g,x)
    else:
        return ValueError("q must be prime")


def sign(m,key):
  
    h = m
    print("---- h= %d"%h)
    p, q, g, x = key

    k = random.randrange(1,q)
    print("k=",k)
    r = modular_exponentiation(g,k,p)%q

    i = math.floor(random.random()*(10**(random.randrange(1,7))))
    
    while (modular_exponentiation(k,i,q)) !=1:
        i+=1
    print("check i %s,%d"%(i, modular_exponentiation(k, i, q)))
    s = (i * (h +r * x)) % q

    check_rs =( r==0 or s ==0)
    print("check_rs",check_rs)
    if check_rs == True:
        sign(m,key)
    else:
        print("check_rs",check_rs)
        print("ádasd",r,s)
        return r,s

def verify(m,key,r,s):
    print(key)
    p, q, g, y = key
    h=m
    w =  math.floor(random.random()*(10**(random.randrange(1,5))))
    while (s*w) % q != 1:
        w +=1
    print("calcu w",w,(s*w) % q )

    u1 = (h * w) % q
    u2 =  (r * w) % q

    v =(((g ** u1) * (y ** u2)) % p) % q
    print(v)
    print(r)
    if v == r:
        return True
    else:
        return False

# pubkey, prikey=generate_key(197)
# print("publickey :%s____private key: %s" %(pubkey,prikey))

pubkey, prikey=(191, 19, 5, 180),(191, 19, 5, 15)
r, s= sign(5, prikey)
print("r-s",r,s)

print(verify(5,pubkey,r,s))
