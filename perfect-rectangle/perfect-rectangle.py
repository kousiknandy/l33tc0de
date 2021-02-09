def area(rect):
    a = (rect[0] - rect[2]) * (rect[1] - rect[3])
    if a < 0:
        a = -a
    return a
    
def minmax_xy(rectangles):
    x1 = 32767
    y1 = 32767
    x2 = -32768
    y2 = -32768
    for rec in rectangles:
        if x1 > rec[0]:
            x1 = rec[0]
        if x1 > rec[2]:
            x1 = rec[2]
        if y1 > rec[1]:
            y1 = rec[1]
        if y1 > rec[3]:
            y1 = rec[3]
        if x2 < rec[0]:
            x2 = rec[0]
        if x2 < rec[2]:
            x2 = rec[2]
        if y2 < rec[1]:
            y2 = rec[1]
        if y2 < rec[3]:
            y2 = rec[3]
    return [x1, y1, x2, y2]

def normalize(rec):
    n = []
    if rec[0] < rec[2]:
        n.append(rec[0])
    else:
        n.append(rec[2])
    if rec[1] < rec[3]:
        n.append(rec[1])
    else:
        n.append(rec[3])
    if rec[0] > rec[2]:
        n.append(rec[0])
    else:
        n.append(rec[2])
    if rec[1] > rec[3]:
        n.append(rec[1])
    else:
        n.append(rec[3])
    return n

def overlap(r1, r2):
    #print(r1, r2)
    if r1[0] >= r2[2] or r2[0] >= r1[2]:
        return False
    if r1[3] <= r2[1] or r2[3] <= r1[1]:
        return False
    r1, r2 = r2, r1
    # print(r1, r2)
    if r1[0] >= r2[2] or r2[0] >= r1[2]:
        return False
    if r1[3] <= r2[1] or r2[3] <= r1[1]:
        return False
    return True

class Solution:
    def isRectangleCover(self, rectangles):
        normals = []
        for rec in rectangles:
            normals.append(normalize(rec))
        rectangles = normals
        ar = 0
        for rec in rectangles:
            ar = ar + area(rec)
        c = minmax_xy(rectangles)
        print(c)
        if area(c) != ar:
            return False
        for r1 in rectangles:
            for r2 in rectangles:
                if (not r1 is r2) and overlap(r1, r2):
                    return False
        return True
    
if __name__ == "__main__":
    S = Solution()
    a = S.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])
    print(a)

    S = Solution()
    a = S.isRectangleCover([[0,0,1,1],[0,1,3,2],[1,0,2,2]])
    print(a)

    S = Solution()
    a = S.isRectangleCover([[0,0,2,2],[1,1,3,3],[2,0,3,1],[0,3,3,4]])
    print(a)

    S = Solution()
    a = S.isRectangleCover([[0,0,2,2],[1,1,3,3],[2,0,3,1],[0,3,3,4]])
    print(a)
