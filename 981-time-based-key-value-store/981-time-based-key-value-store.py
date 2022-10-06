class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key] += [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        items = self.table[key]
        l, r = 0, len(items) - 1
        if not items or timestamp < items[0][0]:
            return ''
        
        elif timestamp > items[-1][0]:
            return items[-1][1]
        
        else:
            while l <= r:
                m = (l+r) // 2
                if timestamp > items[m][0]:
                    l = m + 1
                elif timestamp < items[m][0]:
                    r = m - 1
                else:
                    return items[m][1]
            return items[r][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)