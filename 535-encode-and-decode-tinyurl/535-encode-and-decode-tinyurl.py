class Codec:
    def __init__(self):
        self.url = {}
        self.suffix_set = "abcdefghijklmnopqrstuvwzyz"

    def encode(self, longUrl):
        tiny_url = "http://tinyurl.com/".join(random.choice(self.suffix_set) for _ in range(6))
        self.url[tiny_url] = longUrl
        return tiny_url

    def decode(self, shortUrl):
        return self.url[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))