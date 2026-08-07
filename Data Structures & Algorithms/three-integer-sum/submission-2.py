class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        result = []

        for i in range(len(nums_sorted)-2):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue
            target = -nums_sorted[i]

            left = i+1 #j
            right = len(nums_sorted) - 1 #k

            while left < right:
                total = nums_sorted[left] + nums_sorted[right]
                if total == target:
                    result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])

                    left += 1
                    right -= 1

                    while left < right and nums_sorted[left] == nums_sorted[left-1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                        right -= 1

                elif total > target:
                    right -= 1
                else:
                    left += 1

        return result



        
        