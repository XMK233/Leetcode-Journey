def isPowerOfFour(num):
    ## https: // blog.csdn.net / qq508618087 / article / details / 51279074
    if num <= 0:
        return False
    if (num & (num - 1)):
        return False
    return num % 3 == 1

print(isPowerOfFour(15))