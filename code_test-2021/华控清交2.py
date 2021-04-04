with open(file_name, "r") as fn:
    words = fn.readlines()

dic = {}
for word in words:
    if word[0] != "t":
        continue
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

l = []
for word in dic.keys():
    l.append((word, dic[word]))
l.sort(key=lambda x: x[1])

counter = 0
for tp in l:
    print(tp)
    counter += 1
    if counter == 10:
        break