class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")","{":"}","[":"]"}
        stack=[]
        for ch in s:
            if ch in d:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if ch != d.get(stack.pop()):
                    return False
        return not stack
