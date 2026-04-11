class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        S=set()
        j:int=0
        for i in range(len(nums)):
            if(abs(i-j)>k):
                S.remove(nums[j])
                j+=1
            if(nums[i] in S): return True
            S.add(nums[i])
        return False