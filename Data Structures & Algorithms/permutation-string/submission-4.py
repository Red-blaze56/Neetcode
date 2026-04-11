class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = {}
        for s in s1:
            counter1[s] = counter1.get(s, 0) + 1

        window = len(s1)
        l = 0
        counter2 = {}

        for r in range(len(s2)):
            counter2[s2[r]] = counter2.get(s2[r], 0) + 1

            while r - l + 1 > window:
                left_char = s2[l]
                if left_char in counter2:
                    counter2[left_char] -= 1
                    if counter2[left_char] == 0:
                        counter2.pop(left_char)
                l += 1   # ← ALWAYS move l

            if counter1 == counter2:
                return True

        return False
