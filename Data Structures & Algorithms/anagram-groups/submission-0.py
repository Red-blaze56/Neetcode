class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ord(a) -> function to get ASCII val of letter a ---> 97, b--->98, c --->99; if i want to put c i will find 99-97=2 i.e c at index 2

        res = defaultdict(list)
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1
            res[tuple(count)].append(word)
        return list(res.values())