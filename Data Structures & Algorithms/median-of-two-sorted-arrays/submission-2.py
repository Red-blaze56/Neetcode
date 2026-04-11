class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        if len(num2)<len(num1):
            return self.findMedianSortedArrays(num2, num1)
        
        x = len(num1)
        y = len(num2)

        l=0
        r = x

        while l<=r:
            midx=(l+r)//2
            midy=(x+y+1)//2 - midx

            l1 = float("-inf") if midx==0 else num1[midx-1]
            r1 = float("inf") if midx==x else num1[midx]

            l2 = float('-inf') if midy==0 else num2[midy-1]
            r2 = float('inf') if midy==y else num2[midy]

            if l1<=r2 and l2<=r1:
                if (x+y)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2.0
                else:
                    return max(l1,l2)
            elif l1>r2:
                r=midx-1
            else:
                l=midx+1
        return 0.0
