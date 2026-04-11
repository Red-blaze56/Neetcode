class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        cars=[]
        for i in range(n):
            time=(target-position[i])/speed[i]
            cars.append((position[i],time))
        cars.sort()
        print(cars)
        stack=[]
        for i in range(n-1,-1,-1):
            if stack and cars[i][1]<=stack[-1]:
                continue
            stack.append(cars[i][1])
        return len(stack)