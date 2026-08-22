class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n - 1

        while l<=h:
            m = (l + h) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                h = m - 1
        return -1


        