
import mymath
import random
# def GetE(phi):
#     e = 65537
#     while True:
#         if mymath.GCD_extended(e,phi)[2]==1:
#             break
#     return e

def GetE(phi):
    e=random.randint(1,phi)
    if e %2 ==0:
        e+=1
    while e<phi:
        if mymath.GCD_extended(e,phi)[2]==1:
            break
        e+=2
    return e
def GetD(e,phi):    
    d = mymath.GCD_extended(e,phi)[0]
    if d < 0:
        d+= phi
    return d

def GetPQ():
    f =  open("data/prime.txt", "r")
    p= int(f.readline())
    q =  int (f.readline())
    return p, q


if __name__ == "__main__":
    p,q = GetPQ()
    n =  p*q
    phi= (p-1)*(q-1)
    e = GetE(phi)
    d =  GetD(e,phi)
    print("e=",e)
    print("d=",d)
    f =  open("data/PublicKey1.txt", "w")
    f.write(str(n)+'\n'+str(e))
    f =  open("data/PrivateKey1.txt", "w")
    f.write(str(n)+'\n'+str(d))
