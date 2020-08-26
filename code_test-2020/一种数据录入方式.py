import collections

def howToUseDefaultDict():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

    d = collections.defaultdict(list)
    for k, v in s:
        d[k].append(v)

    dl = list(d.items())
    print(d)
    print(dl)

howToUseDefaultDict()