from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = {0}
        visit = {0}
        n = len(rooms)
        keyque = deque(rooms[0])
        while len(keyque) > 0:
            key = keyque.popleft()
            if key in visit: continue
            visit.add(key)
            keys.add(key)
            newkeys = [k for k in rooms[key] if k not in keys]
            keyque.extend(newkeys)
        return len(visit) == n
