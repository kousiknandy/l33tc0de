from functools import reduce 

class Codec:

    djb2 = lambda _, x: reduce(lambda x,c: (x*33 + ord(c)) & 0xFFFFFFFF, x, 5381)

    def __init__(self):
        self.url_db = defaultdict(list)
        self.prefix = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        k = hex(self.djb2(longUrl))
        self.url_db[k].append(longUrl)
        # print(k)
        return self.prefix + "/" + str(len(self.url_db[k])-1) + "/" + k

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        p = shortUrl.split("/")
        # print(p)
        i, k = p[4], p[5]
        try:
            return self.url_db[k][int(i)]
        except:
            pass
        return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
