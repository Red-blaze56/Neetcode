from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidates = -1
        votes = 0
        for num in nums:
            if votes==0: 
                candidates = num
                votes=1
            elif num==candidates: votes+=1
            else : votes-=1
        # now candidates last updated value is either major element or survivor, so we check it using another loop to see count>n//2    
        count=0
        for num in nums:
            if num==candidates:
                count+=1
        if count>len(nums)//2:
            return candidates
        else: return -1
  