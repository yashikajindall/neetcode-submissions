class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxW = 0

        while left < right:
            width = right - left
            water = width * min(heights[left], heights[right])
            maxW = max(maxW, water)

            if heights[left]< heights[right]:
                left += 1
            
            elif heights[left]> heights[right]:
                right -= 1
            
            else:
                left += 1
                right -= 1

        return maxW




        