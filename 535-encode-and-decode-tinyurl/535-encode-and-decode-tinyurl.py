class Codec:
    def __init__(self):
        self.url = {}

    def encode(self, longUrl):
        suffix_set = "abcdefghijklmnopqrstuvwzyz"
        tiny_url = "http://tinyurl.com/".join(random.choice(suffix_set) for _ in range(6))
        self.url[tiny_url] = longUrl
        return tiny_url

    def decode(self, shortUrl):
        return self.url[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))