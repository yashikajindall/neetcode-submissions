class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for n in range(len(nums)):
            prefix= nums[:n]
            postfix= nums[n+1:len(nums)]        
            product = math.prod(prefix) * math.prod(postfix)
            result.append(product)

        return result

        