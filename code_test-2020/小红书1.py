_items = [_ for _ in input().split()]
# _items = ["5", "2", "C", "T", "+", "-"]
items = []
for item in _items:
    if item.isdigit():
        items.append(int(item))
    else:
        items.append(item)
stack = []
for item in items:
    if type(item) == int:
        stack.append(item)
    elif item == "C":
        if len(stack) == 0:
            continue
        stack.pop(-1)
    elif item == "T":
        if len(stack) == 0:
            continue
        stack.append(stack[-1] * 3)
    elif item == "+":
        if len(stack) < 2:
            continue
        stack.append(sum(stack[-2:]))
    elif item == "-":
        if len(stack) < 2:
            continue
        stack.append(abs(stack[-1] - stack[-2]))
print(sum(stack))