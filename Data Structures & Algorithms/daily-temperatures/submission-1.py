class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stck = []
        
        for i in range(len(temperatures)):
            while stck and temperatures[i] > temperatures[stck[-1]]:
                waiting_days = stck.pop()
                result[waiting_days] = i - waiting_days 
            stck.append(i)

        return result


        