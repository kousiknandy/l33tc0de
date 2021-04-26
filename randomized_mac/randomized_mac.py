from functools import singledispatch
import random
import sys

@singledispatch
def iterates(input):
    for x in input: yield x

@iterates.register
def _(input:str):
    for x in input: yield ord(x)

def hash_djb_2(s, bits=48):                                                                                                                                
    hash = 5381
    for x in iterates(s):
        hash = ((( hash << 5) + hash) + x) & (2**bits - 1)
    return hash


def generate_mac(prefix, target, vendor=b'', bits=48, span=16):
    def djb(prefix, suffix):
        hash = 5381 if not prefix else djb(None, prefix)
        for c in iterates(suffix):
            hash = (hash * 33 + c) & (2**span - 1)
        return hash
    
    startp = (int.from_bytes(vendor, 'big') << len(vendor)*8) 
    start  = startp + random.getrandbits(bits - len(vendor)*8)
    end    = startp + 2**(bits - len(vendor)*8) - 1
    while start < end:
        suffix = start.to_bytes(bits//8, 'big')
        if target == djb(prefix, suffix):
            yield suffix
        start += 1

if __name__ == "__main__":
    secretkey = sys.argv[1] if len(sys.argv) > 1 else "dnac"
    deviceid  = (int(sys.argv[2]) if len(sys.argv) > 2 else 123456) % (2**16-1)
    vendor    = sys.argv[3].encode() if len(sys.argv) > 3 else b'\xFC\xFB\xFB'
    for s in generate_mac(secretkey, deviceid, vendor):
        print(":".join(format(x, '02X') for x in s))
        # print(hash_djb_2(b'\x64\x6e\x61\x63' + s, 16))
