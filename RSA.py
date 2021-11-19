import mymath
import colorama
from colorama import Fore
import hashlib

def GetPublicKey(file):
    f = open(file,"r")
    n = int(f.readline())
    e = int(f.readline())
    return n,e
def GetPrivateKey(file):
    f =  open( file, "r")
    n = int(f.readline())
    d = int(f.readline())
    return n, d


def sign(m, PrivateKey):
    n ,d = PrivateKey
    s =  mymath.md_ex(m, d, n)

    return s

def verify(s, m, PublicKey):

    n, e = PublicKey

    v = mymath.md_ex(s, e, n)
  
    if m == v:
        return True
    else: 
        return False

if __name__ == "__main__":
    PublicKey, PrivateKey = GetPublicKey("data/PublicKey1.txt"), GetPrivateKey("data/PrivateKey1.txt")
    # publickey(n,e)
    print(Fore.RED+"PublicKey:%s\nPrivateKey:%s"%(PublicKey, PrivateKey))
    f=  open("data/ou.txt", "rb")
    M=f.read()
    m= int(hashlib.sha1(M).hexdigest(),16)
    print(Fore.GREEN+ "m =",m)
    s = sign(m,PrivateKey)
    print("chu ki :", s)

    f1=  open("data/ou1.txt", "rb")
    M=f1.read()
    m= int(hashlib.sha1(M).hexdigest(),16)

    print("m':",m)
    
    print("xac nhan van ban:",verify(s,m, PublicKey))