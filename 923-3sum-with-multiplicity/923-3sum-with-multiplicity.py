class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n, MOD = len(arr), 10**9+7
        ans = 0
        seen = defaultdict(int)
        for i in range(n):
            for j in range(i+1, n):
                complement = target - arr[i] - arr[j]
                if complement in seen:
                    ans = (ans + seen[complement]) % MOD
            seen[arr[i]] += 1
        
        return ans