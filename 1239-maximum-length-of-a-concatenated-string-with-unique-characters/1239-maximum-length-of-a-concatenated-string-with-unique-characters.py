class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniqELements = ['']
        maximum = 0
        for i in range(len(arr)):
            for j in range(len(uniqELements)):
                x = arr[i] + uniqELements[j]
                if len(x) == len(set(x)):
                    uniqELements.append(x)
                    maximum = max(maximum, len(x))

        return maximum