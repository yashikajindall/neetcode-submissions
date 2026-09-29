class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = len(position)
        stack = []
        cars = sorted(zip(position, speed), reverse=True)
        
        for p, s in cars:
            t = (target - p) / s
            if stack and t <= stack[-1]:
                result -= 1
            else:
                stack.append(t)
        return result   
