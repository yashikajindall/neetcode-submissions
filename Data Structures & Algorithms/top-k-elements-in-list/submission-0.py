class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1 

        sorted_function = sorted(count, key = lambda num: count[num], reverse = True)

        return sorted_function[:k]



        