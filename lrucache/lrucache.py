class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.current = 0
        self.sentinel = object()
        self.lru_list = {}
        self.lru_list["PREV"] = self.lru_list
        self.lru_list["NEXT"] = self.lru_list
        self.lru_list["KEY"]  = None
        self.lru_list["VALUE"] = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        lru_elem = self.cache.get(key, self.sentinel)
        if lru_elem is self.sentinel:
            return None
        lru_elem["PREV"]["NEXT"] = lru_elem["NEXT"]
        lru_elem["NEXT"]["PREV"] = lru_elem["PREV"]
        lru_elem["NEXT"] = self.lru_list["NEXT"]
        lru_elem["PREV"] = self.lru_list
        self.lru_list["NEXT"] = lru_elem
        return lru_elem["VALUE"]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        new_elem = self.cache.get(key, self.sentinel)
        if new_elem is self.sentinel:
            if self.current == self.capacity:
                evict = self.lru_list["PREV"]
                print(evict)
                self.lru_list["PREV"] = evict["PREV"]
                evict["PREV"]["NEXT"] = self.lru_list
                del self.cache[evict["KEY"]]
                new_elem = evict
            else:
                new_elem = {}
                self.current += 1
        else:
            new_elem["PREV"]["NEXT"] = new_elem["NEXT"]
            new_elem["NEXT"]["PREV"] = new_elem["PREV"]
        new_elem["PREV"] = self.lru_list
        new_elem["NEXT"] = self.lru_list["NEXT"]
        new_elem["KEY"] = key
        new_elem["VALUE"] = value
        self.lru_list["NEXT"] = new_elem
        print(" ", new_elem, " // ", self.lru_list)
        self.cache[key] = new_elem

    def __repr__(self):
        s = "(" + str(self.capacity) + ", " + str(self.current) + "): "
        e = self.lru_list
        for i in range(self.current):
            e = e["NEXT"]
            s += str(e["KEY"]) + "," + str(e["VALUE"]) + "->"
        return s
        
LC = LRUCache(4)
print(LC)
LC.put('a', ord('a'))
LC.put('b', ord('b'))
print(LC)
print(LC.get('b'))
LC.put('b', ord('B'))
print(LC)
print(LC.get('b'))
LC.put('c', ord('c'))
LC.put('d', ord('d'))
print(LC)
LC.put('e', ord('e'))
print(LC)
