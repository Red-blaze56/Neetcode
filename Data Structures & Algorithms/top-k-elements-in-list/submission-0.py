class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = dict()
        res = list()
        for i in nums:
            D[i]=D.get(i,0)+1
        for _ in range(k):
            for key,val in D.items():
                max_key = max(D, key=D.get)
            res.append(max_key)
            del D[max_key]
        return res