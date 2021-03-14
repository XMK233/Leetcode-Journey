import os

oldCoreNames = []
oldPath = r"C:\Users\XMK23\Documents\Leetcode-Journey\NowcoderProblems"
for i in os.listdir(oldPath):
    if "-" not in i:
        continue
    coreName = i[:-3]
    oldCoreNames.append(coreName)
    # if coreName not in newCoreNames:
    #     continue
    # with open(os.path.join(oldPath, i), "r") as f:
    #     lines = f.readlines()
    #     print(lines)

failed = oldCoreNames.copy()

newPath = r"C:\Users\XMK23\Documents\Leetcode-Journey\NowcoderProblems_1"
for i in os.listdir(newPath):
    if "-" not in i:
        continue
    newCoreName = "-".join(i.split("-")[0:2])
    # newCoreNames.append(newCoreName)
    if newCoreName not in oldCoreNames:
        continue
    lines = None
    with open(os.path.join(oldPath, newCoreName + ".py"), "r", encoding="utf-8") as source:
        lines = source.readlines()
    with open(i, "a", encoding="utf-8") as destiny:
        destiny.write("".join(lines))
    print(newCoreName, i)
    failed.remove(newCoreName)
    # break

# print("\n\n", failed)
