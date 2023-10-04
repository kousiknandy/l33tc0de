from functools import reduce 

class Codec:

    djb2 = lambda _, x: reduce(lambda x,c: (x*33 + ord(c)) & 0xFFFFFFFF, x, 5381)

    def __init__(self):
        self.url_db = defaultdict(list)
        self.prefix = "http://tinyurl.com/"
        self.url_list = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if False:
            k = hex(self.djb2(longUrl))
            self.url_db[k].append(longUrl)
            return self.prefix + "/" + str(len(self.url_db[k])-1) + "/" + k
        self.url_list.append(longUrl)
        return self.prefix + "/" + str(len(self.url_list)-1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        p = shortUrl.split("/")
        if False:
            i, k = p[4], p[5]
            try:
                return self.url_db[k][int(i)]
            except:
                pass
                return None
        return self.url_list[int(p[4])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
