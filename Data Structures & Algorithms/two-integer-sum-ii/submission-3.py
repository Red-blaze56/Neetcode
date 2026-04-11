class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = []
        res = []
        for i,num in  enumerate(numbers):
            if visited and  visited[0]==num:
                res.append(i+1)
                break
            if len(visited)==0 and target - num in numbers:
                visited.append(target-num)
                res.append(i+1)
        return res 