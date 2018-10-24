def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L


def apply():
    testList = [1, -4, 8, -9]

    def f(x):
        return x+1

    return applyToEach(testList, f)
