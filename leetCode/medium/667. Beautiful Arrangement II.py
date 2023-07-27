def constructArray(n, k):
    i, j = 1, n
    result = []
    while i <= j and k > 1:
        if k > 1:
            if k % 2 == 1:
                result += [i]
                i += 1
            else:
                result += [j]
                j -= 1
            k -= 1
    for z in range(i, j+1):
        result += [z]
    printDistance(result)
    return result


def printDistance(inputs):
    myList = []
    for i in range(len(inputs) - 1):
        myList += [abs(inputs[i] - inputs[i + 1])]
    print(myList)


print(constructArray(9, 5))
# printDistance([1, 5, 2, 4, 3])
