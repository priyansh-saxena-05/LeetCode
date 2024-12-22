from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            freq = [0]*26
            for char in s:
                freq[ord(char)-ord('a')] += 1
            hmap[(str(freq))].append(s)
        return list(hmap.values())
        