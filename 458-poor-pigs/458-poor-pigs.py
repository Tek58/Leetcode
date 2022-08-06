class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        return int(ceil(log(buckets) / log(minutesToTest // minutesToDie + 1)))
        