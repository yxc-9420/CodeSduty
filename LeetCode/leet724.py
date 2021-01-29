from functools import reduce
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int])-> int:
        all = reduce(lambda x,y:x+y,nums)
        he = 0
        for i in range(len(nums)):
            he = he + nums[i]
            if (he*2-nums[i])==all:
                return i
        return -1 

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,7,6,5,6]
    print(s.pivotIndex(nums))