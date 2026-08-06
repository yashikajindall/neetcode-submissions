class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(set(nums))
        current = 1
        longest = 1

        if nums == []:
            return 0 
        
        for i in range(len(nums_sorted)-1):
            if nums_sorted[i + 1] - nums_sorted[i] == 1:
                current += 1
            else:
                current = 1
            
            longest = max(longest,current)

        return longest 
        