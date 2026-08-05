class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num_1 = target - nums[i]
            if num_1 in nums:
                j = nums.index(num_1)
                if i != j:
                    return sorted([i,j])