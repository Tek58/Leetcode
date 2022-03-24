class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        count = 0
        while left <= right:
            count += 1
            val = people[left] + people[right]
            if val <= limit:
                left += 1
            right -= 1
        return count
                
                
                