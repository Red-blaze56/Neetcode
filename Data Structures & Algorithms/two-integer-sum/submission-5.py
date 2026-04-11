class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = dict()
        for i,n in enumerate(nums):
            dic[n]=i

        for i,n in enumerate(nums):
            diff = target-n
            if (diff) in dic and dic[diff]!=i:
                return [i,dic[diff]]
        return []

        extra = dict()
        for i,n in enumerate(nums):
            diff = target-n
            if diff in extra:
                return [extra[diff]]
            extra[n]=i
        return [] 