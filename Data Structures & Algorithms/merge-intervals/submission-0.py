class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1: return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        for itv in intervals:
            if not res or res[-1][1]<itv[0]:
                res.append(itv)
            else:
                res[-1][1] = max(res[-1][1],itv[1])
        return res