class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                second_val = int(stack.pop())
                first_val = int(stack.pop())
                new_val = ""
                if i == "+":
                    new_val = first_val + second_val
                elif i == "-":
                    new_val = first_val - second_val
                elif i == "*":
                    new_val = first_val * second_val
                else:
                    new_val = first_val / second_val
                stack.append(new_val)
            else:
                stack.append(i)
        return int(stack[-1])
                
                
        