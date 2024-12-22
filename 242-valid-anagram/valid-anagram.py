class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1
        
        print(freq)

        for ch in t:
            idx = ord(ch) - ord('a')
            freq[idx] -= 1
        
        print(freq)
        
        for i in freq:
            if i != 0:
                return False
        
        return True
