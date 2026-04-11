class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n = len(s)
        letters1={}
        letters2={}
        for i in range(n):
            letters1[s[i]] = letters1.get(s[i],0)+1
            letters2[t[i]] = letters2.get(t[i],0)+1
        return True if letters1==letters2 else False

