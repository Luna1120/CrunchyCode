N-Repeated Element in Size 2N Array:

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length1=len(nums)
        n=length1/2
        for i in nums:
            if n==nums.count(i):
                return i
            else:
                continue
