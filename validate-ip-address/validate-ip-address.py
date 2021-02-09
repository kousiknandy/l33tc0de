class Solution:
    def validIPAddress(self, IP: str) -> str:
        v4 = IP.split(".")
        if len(v4) == 4:
            for i in range(4):
                if len(v4[i]) == 0:
                    return "Neither"
                if v4[i][0] == "0":
                    if len(v4[i]) == 1:
                        continue
                    return "Neither"
                try:
                    oc = int(v4[i])
                    if 1 > oc or 255 < oc:
                        return "Neither"
                except:
                    return "Neither"
            else:
                return "IPv4"
            
        v6 = IP.split(":")
        if len(v6) == 8:
            for i in range(8):
                if len(v6[i]) == 0 or len(v6[i]) > 4:
                    return "Neither"
                try:
                    oc = int(v6[i], 16)
                except:
                    return "Neither"
            else:
                return "IPv6"

        return "Neither"

S = Solution()
a = "10.0.0.1"
print(a, S.validIPAddress(a))
a = "10.10.20.41"
print(a, S.validIPAddress(a))
a = "10.0.300.1"
print(a, S.validIPAddress(a))
a = "10.0007.0.1"
print(a, S.validIPAddress(a))
a = "10..."
print(a, S.validIPAddress(a))
a = "256.256.256.256"
print(a, S.validIPAddress(a))

a = "2001:0db8:85a3:0:0:8A2E:0370:7334"
print(a, S.validIPAddress(a))
a = "02001:0db8:85a3:0000:0000:8a2e:0370:7334"
print(a, S.validIPAddress(a))

