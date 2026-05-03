# Postfix expression evaluation 

"""
rules:
1. Scan given expression from left to right
2. if element == operand push it
3. if element == operator: 
    1. pop top 2 operands
    2. peroform operation
    3. push back result 

4. repeat until complete scan
5. pop the result

"""

x = 8 3 - 4 2 + * 9 3 / + 
s = []
y = 33

# answer is 33