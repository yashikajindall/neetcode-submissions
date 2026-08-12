class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        pairs = {'{':'}', '(':')', '[':']'}
        
        for char in s:
            if char in pairs:
                stck.append(char)
            else:
                if not stck:
                    return False

                opening = stck.pop()

                if pairs[opening] != char:
                    return False

        return stck == []

