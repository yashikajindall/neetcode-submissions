class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        longest = 1

        if not nums:
            return 0

        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)-1):   
            if sorted_nums[i+1] == sorted_nums[i]:
                continue
            if sorted_nums[i + 1] == sorted_nums[i] + 1:
                count = count + 1
                longest = max(count, longest)
            else:
                count = 1
        return longest     