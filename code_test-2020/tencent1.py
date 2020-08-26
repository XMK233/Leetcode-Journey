signs = ")([]]([(](])))([]()()]([][[)[()[)]([[(])][][[[([)]"
import collections
# stack = collections.defaultdict(list)
stack_round = []
stack_square = []
for sign in signs:
    if sign == "(":
        stack_round.append(sign)
    elif sign == ")":
        if len(stack_round) == 0:
            stack_round.append(sign)
        else:
            if stack_round[-1] == "(":
                stack_round.pop(-1)
            else:
                stack_round.append(sign)
    elif sign == "[":
        stack_square.append(sign)
    elif sign == "]":
        if len(stack_square) == 0:
            stack_square.append(sign)
        else:
            if stack_square[-1] == "[":
                stack_square.pop(-1)
            else:
                stack_square.append(sign)

print(stack_round)
print()
print(len(stack_square) + len(stack_round))
# print(len(stack_round))
    # if sign == "(" or sign == ")":
    #     if len(stack_round) == 0:
    #         stack_round.append(sign)
    #     else:
    #         if sign == "(":
    #             if stack_round[-1]