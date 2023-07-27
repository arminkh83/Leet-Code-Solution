def isPalindrome(x):
    if x < 0:
        return False
    myNumber = str(x)
    down = 0
    up = len(myNumber) - 1
    while up > down:
        if myNumber[up] != myNumber[down]:
            return False
        down += 1
        up -= 1
    return True


print(isPalindrome(-13))