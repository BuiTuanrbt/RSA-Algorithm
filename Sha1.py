import struct
import hashlib



def left_rotate(n, b):
    """Left rotate a 32-bit integer n by b bits."""
    return ((n << b) | (n >> (32 - b)))  & 0xffffffff


def sha1(message):
    # message= message.encode('ASCII')
   
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    byte_len = len(message)
    
    bit_len =  byte_len*8
    # add bit '1'
    message += b'\x80' 
    
    message += b'\x00' * (56 - (byte_len+1) )

    message += struct.pack(b'>Q', bit_len)
    w = [0] * 80
    for i in range(16):
        w[i] = struct.unpack(b'>I', message[i*4:i*4 + 4])[0]
    for i in range(16, 80):
        w[i] = left_rotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1)
    
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    for i in range(80):
        if 0 <= i <= 19:
            # Use alternative 1 for f from FIPS PB 180-1 to avoid ~
            f = d ^ (b & (c ^ d))
            k = 0x5A827999
        elif 20 <= i <= 39:
            f = b ^ c ^ d
            k = 0x6ED9EBA1
        elif 40 <= i <= 59:
            f = (b & c) | (b & d) | (c & d) 
            k = 0x8F1BBCDC
        elif 60 <= i <= 79:
            f = b ^ c ^ d
            k = 0xCA62C1D6

        a, b, c, d, e = ((left_rotate(a, 5) + f + e + k + w[i]) & 0xffffffff, 
                            a, left_rotate(b, 30), c, d)
    
    h0 = (h0 + a) & 0xffffffff
    h1 = (h1 + b) & 0xffffffff 
    h2 = (h2 + c) & 0xffffffff
    h3 = (h3 + d) & 0xffffffff
    h4 = (h4 + e) & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

    
if __name__=='__main__':
    f = open("prime.txt", "rb")
    M = f.read()
    a="abc"
    b = str(a).encode('utf-8')
    
    print(hashlib.sha1("abc").hexdigest())
    print(sha1("abc"))