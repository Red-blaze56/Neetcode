from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.StoreMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.StoreMap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        if key not in self.StoreMap:
            return res
        values = self.StoreMap.get(key,[])
        l, h = 0, len(values)-1
        while l<=h:
            mid=l+(h-l)//2
            if values[mid][0]<=timestamp:
                res = values[mid][1]
                l=mid+1
            else:
                h=mid-1
        return res
            

        

