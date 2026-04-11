class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + "#" + s 
        return res

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            l = int(s[i:j])
            res.append(s[j+1:j+l+1])
            i = j+l+1

        return res

