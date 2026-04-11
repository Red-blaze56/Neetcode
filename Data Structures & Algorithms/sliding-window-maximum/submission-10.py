from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res=[]
        for i, curr in enumerate(nums):
            while d and nums[d[-1]]<=curr:
                d.pop()
            d.append(i)
            if d[0]<=i-k:
                d.popleft()
            if i>=k-1:
                res.append(nums[d[0]])
        return res




