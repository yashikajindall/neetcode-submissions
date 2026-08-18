class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                add = stack.pop() + stack.pop()
                stack.append(add)
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                subtract = b - a 
                stack.append(subtract)
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                divide = b/a
                stack.append(int(divide))
            elif i == "*":
                multiply = stack.pop() * stack.pop()
                stack.append(multiply)
            else:
                stack.append(int(i))
        return stack[0]
                


        