class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        best = 1
        
        if not s:
            return 0
        
        for i in range(len(s)):
                while s[i] in seen:
                    seen.discard(s[left])
                    left += 1
                seen.add(s[i])
                best = max(len(seen), best)
        
        return best
            
            


        