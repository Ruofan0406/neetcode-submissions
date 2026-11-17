class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c != "+" and c != "-" and c!= "*" and c != "/":
                stack.append(int(c))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if c == "+":
                    temp = a+b
                elif c == "-":
                    temp = a-b
                elif c == "*":
                    temp = a*b
                else:
                    temp = int(a/b)
                stack.append(temp)
        
        return stack[-1]