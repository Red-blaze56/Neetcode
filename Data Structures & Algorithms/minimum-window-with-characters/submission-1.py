class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count={}
        for char in t:
            count[char] = count.get(char,0)+1
        
        l=0
        win={}
        result=""
        have=0
        required = len(count)
        winlen=101001010100
        for r in range(len(s)):
            char = s[r]
            if char in count: 
                win[char] = win.get(char, 0) + 1
                
                if win[char] == count[char]:
                    have += 1
            
            while l <= r and have == required:
                if r-l+1 < winlen:
                    winlen=r-l+1
                    result="".join(s[l:r+1])
                left_char = s[l]
                if left_char in count:
                    win[left_char] -= 1
                    if win[left_char] < count[left_char]:
                        have -= 1
                l += 1

        return result
            


