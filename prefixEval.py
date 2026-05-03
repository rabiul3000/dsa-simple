# Prefix expression evaluation 

"""
rules:
1. Scan given expression from right to left
2. if operand, push to the stack
3. if operator:
    1. pop top 2 operands
    2. perform operation
    3. push back result

4. repeat 2 and 3 until complete scan
5. pop the result

|  s1   | 
|_______|       
|  s2   |          
|_______|
s1 op s2
"""

x = +*-73//92+43 
s = []
y = 23

# answer is 23