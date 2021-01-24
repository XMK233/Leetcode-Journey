## The code is in python.

def arithmeticExpParser(s_):
    ## remove the unnecessary spaces.
    s = s_.strip()
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif ord(c) >= ord('0') and ord(c) <= ord('9'):
            stack.append(int(c))
        elif c == ')':
            operand2 = stack.pop(-1)
            operator = stack.pop(-1)
            operand1 = stack.pop(-1)
            stack.pop(-1) ## pop the last "("
            if operator == "+":
                stack.append(operand1 + operand2)
            elif operator == "-":
                stack.append(operand1 - operand2)
            elif operator == "*":
                stack.append(operand1 * operand2)
            else: ## the operator is /
                stack.append(operand1 / operand2)
        else:
            stack.append(c)
    return float(stack[0])

print(arithmeticExpParser("((1+0)*(3+(4*5)))"))

