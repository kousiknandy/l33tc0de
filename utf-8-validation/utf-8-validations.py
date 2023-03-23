class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        c_mask = (0b10000000, 0b11000000)
        utf8_mask = [(0b11110000, 0b11111000, 3),
            (0b11100000, 0b11110000, 2),
            (0b11000000, 0b11100000, 1),
            (0b00000000, 0b10000000, 0)]
        idx = 0
        l = len(data)
        while idx < l:
            for m, b, c in utf8_mask:
                if (data[idx] & b) == m:
                    if idx + c >= l: return False
                    idx += 1
                    for j in range(c):
                        if data[idx] & c_mask[1] != c_mask[0]: return False
                        idx += 1
                    break
            else:
                return False
        return True
