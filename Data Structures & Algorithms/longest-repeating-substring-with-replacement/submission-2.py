class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        D = {}
        n = len(s)
        l=r=res=0
        winLen = MaxCount = 0
        for r in range(n):
            D[s[r]] = D.get(s[r],0) + 1
            winLen = r-l+1
            MaxCount = max(MaxCount,D[s[r]]) 
            
            if winLen - MaxCount > k:
                D[s[l]] -= 1
                l+=1

            res = max(res,r-l+1)
        return res

        