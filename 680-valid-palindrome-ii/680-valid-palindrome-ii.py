class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left, right, removed=False):
            while left <= right:
                leftVal = s[left]
                rightVal = s[right]
                if leftVal != rightVal:
                    if removed:
                        return False
                    return check(left+1, right, True) or check(left, right-1, True)
                right -= 1
                left += 1
            return True
        return check(0, len(s)-1)
                