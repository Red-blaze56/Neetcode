class Solution:
    def productExceptSelf(self, nums):
        prefix = [0]*len(nums)
        postfix = [0]*len(nums) 
        res = [0]*len(nums)
        premul = postmul = 1

        for i in range(len(nums)):
            premul *= nums[i]
            prefix[i] = premul
        print(prefix)

        for i in range(len(nums)-1,-1,-1):
            postmul *= nums[i]
            postfix[i] = postmul

        print(prefix)
        for i in range(len(nums)):
            pre = suf = 1
            pre = prefix[i-1] if (i-1)>=0 else 1
            print(prefix[i-1])
            suf = postfix[i+1] if (i+1)<len(nums) else 1
            print(pre,"*",suf)
            res[i] = pre*suf
        return res
        
