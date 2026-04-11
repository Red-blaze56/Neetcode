from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        t=0
        low = 1
        high = max(piles)        
        while low<high:
            k = low + (high-low)//2
            t=0
            for p in piles:
                t+= ceil(p/k)
            if t<=h:
                high=k
            else:
                low=k+1
        return low
