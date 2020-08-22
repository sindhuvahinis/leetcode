def xorOperation(self, n, start):
    res = start
    for i in range(1, n):
        res = res ^ (start + 2 * i)
    return res