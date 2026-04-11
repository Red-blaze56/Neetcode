class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        sd=dict()
        td=dict()
        for er in s:
            if er in sd:
                sd[er]+=1
            else:
                sd[er]=1
        
        for jr in t:
            if jr in td:
                td[jr]+=1
            else:
                td[jr]=1 

        if sd==td:
            return True
        else:
            return False