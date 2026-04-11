class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
 

        extra = dict()
        for i,n in enumerate(nums):
            diff = target-n
            if diff in extra:
                return [extra[diff],i]
            extra[n]=i 
        return []