class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t in ['+','-','*','/']:
                b=(stack.pop())
                a=(stack.pop())
                print(a,b,t)
                match t:
                    case "+":
                        stack.append(a+b)
                    case "-":
                        stack.append(a-b)
                    case "*":
                        stack.append(a*b)
                    case "/":
                        stack.append(int(a/b))
                print(stack)
            else:
                stack.append(int(t))
        return round(stack[0])