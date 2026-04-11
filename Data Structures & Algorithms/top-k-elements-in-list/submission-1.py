class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = dict()
        for i in nums:
            D[i]=D.get(i,0)+1

        arr=[]
        for num,freq in D.items():
            arr.append([freq,num])
        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res

