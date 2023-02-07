class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        next = 0
        max = 0
        bucket = set()
        while j < len(fruits):
            if len(bucket) < 2 or fruits[j] in bucket:
                if len(bucket) == 1 and fruits[j] not in bucket:
                    next = j
                bucket.add(fruits[j])
                j += 1
            else:
                bucket = set()
                if j - i > max:
                    max = j - i
                i = j = next            
        if j - i> max:
            max = j - i
        return max        