class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        ans = ""
        ans += chars[0] 
        for i in range(1, len(chars)):
            if chars[i-1] == chars[i]:
                count +=1
            else:
                if count > 1:
                    ans += str(count)
                ans += chars[i]
                count = 1
        if count > 1:
            ans += str(count)
        for i, char in enumerate(ans):
            chars[i] = char
        return len(ans)
                    

        
