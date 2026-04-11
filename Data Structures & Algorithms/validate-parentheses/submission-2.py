class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")","{":"}","[":"]"}
        stack=[]
        for B in s:
            
            print(f"{B=}")
            if stack and B not in d and B!=d.get(stack[-1]):
                print(d.get(stack[-1]))
                return  False
            if stack and d.get(stack[-1])==B:
                stack.pop()
            else:
                stack.append(B)
            print(f"{stack=}")
        return False if stack else True