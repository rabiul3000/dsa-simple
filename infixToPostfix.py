# infix to postfix conversation
"""
question: let x be the infix expression and y be the postfix expression,
and s is the empty stack

rules
1. Scan element of x one by one from left to right.
2. If element == operand(letter, number) then add to the y directly.
3. if element == ( then push it to the s.
4. if element == closing bracket => ) start pop elements from s and add to the y until you found opening bracket => ( in s. 
5. if element == operator, then check top of stack-
    if stack is empty Push the operator to the stack
    if top of the s is a opening bracket => ( then also Push the operator
    if top of the s has other operators beside ) then:
        if top of s has >= presidency then the x's operator, pop that top of s operator and add it to the y
        if top of s has < presidency then the x's operator, push that operator to the s 
 
6. repeat 2,3,4,5 steps until scanning x is complete. then if s has any elements left over pop all them and add to the y.
7. after all the operation the y will be the postfix expression

simple rules:
step a:
    1. Operands (A, B, 1, 2): They are the VIPs. They go straight to the Output immediately.
    2. Opening bracket (: Always goes to the Stack.
    3. Closing Bracket ): Triggers a cleanup. Pop everything from the Stack to the Output until you hit the matching (.
     Then, throw both brackets away.
step b:
When an operator  + or * wants to enter the Stack, it looks at who is already sitting at the Top:
    4. If the Stack is empty or contains a (: Just push the operator in.
    5. If the new operator is "Stronger" (Higher Precedence) than the one on top: Push it in.
    6. If the new operator is "Weaker" or "Equal": The guy on the stack is "boss."
    Pop the boss to the Output. Keep checking the next item on the stack until you find someone weaker or the stack is empty,
    then push the new operator.



"""
s=[]
x = a+b*(c-d/e)+f
y= a b c d e / - * + f +  