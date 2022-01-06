class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        store = []
        for n, start, end in trips:
            store.append((start, n))
            store.append((end, -n))
        store.sort()
        for i in store:
            capacity -= i[1]
            if capacity < 0:
                return False
        return True