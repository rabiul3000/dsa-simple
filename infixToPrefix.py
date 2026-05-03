"""
Operands (A, B, 1, 2): They are the VIPs. 
They go straight to the Output immediately 
(but since we are moving backward, they will fill the output from right to left).

Closing Bracket ): In this mode, the closing bracket is the "starter." Push it to the Stack.

Opening Bracket (: This is now the "cleanup" trigger. 
Pop everything from the Stack to the Output until you hit the matching ).
Then, throw both away.

Step B: The Operator "Boss" Rule
When an operator wants to enter the Stack, it looks at the Top:
4.  If the Stack is empty or contains a ): Just Push it in.
5.  If the new operator is "Stronger" (Higher Precedence) than the one on top: Push it in.
6.  If the new operator is "Weaker": The guy on the stack is "boss." Pop him to the Output. Keep checking until you find someone weaker, equal, or the stack is empty, then push the new operator.
7.  If the new operator is "Equal": No fight! In Prefix mode, equal operators can sit on top of each other. Push it in.


"""



x = A / B ^ C - (D * E + F)
s = []
y = -/A^BC+*DEF


