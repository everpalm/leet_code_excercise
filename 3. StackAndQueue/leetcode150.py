'''
150. Evaluate Reverse Polish Notation
Medium

Topics
Companies
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9


Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        my_operators = {'+', '-', '*', '/'}
        my_stack = []
        # result = 0
        for token in tokens:
            if token not in my_operators:
                my_stack.append(int(token))
            else:
                # var2 = int(my_stack.pop())
                # var1 = int(my_stack.pop())
                var2 = my_stack.pop()
                var1 = my_stack.pop()
                print(f'var1 = {var1}, var2 = {var2} ')
                if token == '+':
                    # result = var1 + var2
                    my_stack.append(var1 + var2)
                    print('+ result = ', my_stack[-1])
                elif token == '-':
                    # result = var1 - var2
                    my_stack.append(var1 - var2)
                    print('- result = ', my_stack[-1])
                elif token == '*':
                    # result *= int(my_stack.pop())
                    # result = var1 * var2
                    my_stack.append(var1 * var2)
                    print('* result = ', my_stack[-1])
                elif token == '/':
                    if var1 == 0:
                        return False
                    # result, remainder = divmod(var1,  var2)
                    my_stack.append(int(var1 / var2))
                    # result /= int(my_stack.pop())
                    # print('/ result = ', my_stack[-1])
        return my_stack[0]
        # stack = []
        # for token in tokens:
        #     if token in "+-*/":
        #         b = stack.pop()
        #         a = stack.pop()
        #         if token == '+':
        #             stack.append(a + b)
        #         elif token == '-':
        #             stack.append(a - b)
        #         elif token == '*':
        #             stack.append(a * b)
        #         elif token == '/':
        #             # Perform integer division with truncation towards zero
        #             stack.append(int(a / b))
        #     else:
        #         stack.append(int(token))
        
        # return stack[0]



# tokens = ["2","1","+","3","*"]
# my_solution = Solution()
# print('Result = ', my_solution.evalRPN(tokens))

# tokens = ["4","13","5","/","+"]
# my_solution = Solution()
# print('Result = ', my_solution.evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
my_solution = Solution()
print('Result = ', my_solution.evalRPN(tokens))