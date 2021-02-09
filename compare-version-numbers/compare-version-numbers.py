class Solution:
    def subversions(self, vstr):
        l = len(vstr)
        i = 0
        while i < l:
            d = vstr.find('.', i)
            if d == -1:
                ver = vstr[i:]
                i = l
            else:
                ver = vstr[i:d]
                i = d+1
            yield int(ver) if ver else 0

        while True:
            yield None
        
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = self.subversions(version1)
        ver2 = self.subversions(version2)
        while True:
           v1 = next(ver1)
           v2 = next(ver2)
           if v1 is None and v2 is None: return 0
           if v1 is None: v1 = 0
           if v2 is None: v2 = 0
           if v1 > v2:
               return 1
           elif v2 > v1:
               return -1
           
            
S = Solution()
# v = S.subversions("11.002.0..4.02")
# for i in range(7): print(next(v)) # 

print(S.compareVersion("1.2.3", "2.3"))  # -1
print(S.compareVersion("1.2.3", "1.2.3")) # 0
print(S.compareVersion("1.2.3", "1.2.003")) # 0
print(S.compareVersion("1", "2.3")) # -1
print(S.compareVersion("1", "1.2.3")) # -1
print(S.compareVersion("1.", "1.0.0.0")) # 0
print(S.compareVersion("1.1", "1.0.1.0")) # 1
print(S.compareVersion("1.2.3.4.5", "1.2.3.4.6")) # -1
print(S.compareVersion("1.2.3.4.50", "1.2.3.4.6")) # 1

