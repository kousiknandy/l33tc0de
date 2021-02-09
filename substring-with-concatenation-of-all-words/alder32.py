import zlib

def rolling_adler32(st, l=None, r=None, cksum=1):
    MODADLER = 65521
    if cksum == 1:
        a = 1
        b = 0
    else:
        a = cksum & 0xffff
        b = (cksum & 0xffff0000) >> 16
        print("{:8x} {:8x}".format(a, b))
        if l and r:
            a += (r - l)
            a = a % MODADLER
            b += r
            b -= (1+len(st)) * l
            for x in st:
                b += ord(x[0])
            b = b % MODADLER
            return (b << 16) + a
    for x in st:
        a = (a + ord(x[0])) % MODADLER
        b = (a + b) % MODADLER
    return (b << 16) + a

if __name__ == "__main__":
    s1 = zlib.adler32(b"abcdef1234")
    # s2 = zlib.adler32(b"wxyz098765", s1)
    # s3 = zlib.adler32(b"abcdef1234wxyz098765")
    # s4 = zlib.adler32(b"a")
    # s5 = zlib.adler32(b"bcdef1234", -s4)
    # s6 = zlib.adler32(b"5", s5)
    # s7 = zlib.adler32(b"bcdef1234")
    # s8 = zlib.adler32(b"bcdef12345")
    # s9 = zlib.adler32(b"bcdef12345", -s4)
    # print(s1, s2, s3, s4, s5, s6, s7, s8, s9)
    s2 = rolling_adler32("abcdef1234")
    print("{:16x} {:16x}".format(s1, s2))
    s3 = zlib.adler32(b"bcdef12345")
    s4 = rolling_adler32("bcdef1234", ord("a"), ord("5"), s2)
    print("{:16x} {:16x}".format(s3, s4))
    print(zlib.adler32(b"foobar"), zlib.adler32(b"barfoo"))
    
    s1 = rolling_adler32("barfoo")
    s2 = rolling_adler32("arfoo", ord("b"), ord("t"))
    s3 = rolling_adler32("arfoot")
    print(s1, s2, s3)
    
    s1 = rolling_adler32("oobarthef")
    s2 = rolling_adler32("foothebar")
    print(s1, s2)
    
