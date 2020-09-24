## 暴力求解吧.
# n = int(input())
# cards_origin = input().split()
#############################
n = 2
cards_origin = "SA HA".split()
#############################

# zuheOrder = ["HuangJiaTongHuaShun", "TongHuaShun", "SiTiao", "HuLu",
#               "TongHua", "ShunZi" "SanTiao" "LiangDui" "YiDui", "GaoPai"]
cardOrder = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
def isShun(cards):
    nums = [cardOrder.index(card) for card in cards]
    minNum = min(nums)
    maxNum = max(nums)
    actualSumNum = sum(nums)
    expectSumNum = (minNum + maxNum) * (maxNum - minNum + 1) // 2
    if actualSumNum == expectSumNum:
        return True
    else:
        return False

# print(isShun([2, 3, 5]))
# print(isShun([2, 3, 4, 5]))
# print(isShun(["A", 3, 5]))
# print(isShun(["J", "Q", "K"]))
# print(isShun(["J", "Q", 10]))

import collections
huaseClass = collections.defaultdict(list)
for card in cards_origin:
    huaseClass[card[0]].append(card[1:])
numberClass = collections.defaultdict(list)
for card in cards_origin:
    numberClass[card[1:]].append(card[0])

from itertools import combinations
# print(huaseClass)
# print(numberClass)

def judgement():
    for huase in huaseClass:
        cards = huaseClass[huase]
        ## 皇家同花顺
        if "A" in cards and "K" in cards and "Q" in cards and "J" in cards  and "10" in cards:
            return "HuangJiaTongHuaShun"

        ## 同花顺
        if len(cards) >= 5:
            for comb in combinations(cards, 5):
                if isShun(comb):
                    return "TongHuaShun"

    ## 四条
    for number in numberClass:
        huases = numberClass[number]
        huases_set = set(huases)
        if len(huases_set) >= 4:
            return "SiTiao"

print(judgement())