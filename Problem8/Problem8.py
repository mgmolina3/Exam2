import math

def minSquares(n: int):
    if n == 1 or n == 2 or n == 3:
        return n
    if n == 4:
        return 1
    breakDown = []
    breakDown.append(4)
    sum = 4
    while sum != n:
        if sum + 4 > n:
            breakDown.append(1)
            sum += 1
        else:
            breakDown.append(4)
            sum += 4
    
    sum = breakDown[-1]
    popIndexes = 1
    i = len(breakDown)-2
    while i > 0:
        sum += breakDown[i]
        popIndexes += 1
        if math.isqrt(sum) ** 2 == sum:
            while popIndexes > 0:
                breakDown.pop()
                popIndexes -= 1
            breakDown.append(sum)
            i = len(breakDown)-2
            sum = 0
        if len(breakDown) == 2 or len(breakDown) == 3:
            break

    return len(breakDown)

def main():
    print(minSquares(5))
    #print(minSquares(6))
    #print(minSquares(7)) does not work
    #print(minSquares(8))
    #print(minSquares(12))
    #print(minSquares(13))

if __name__==("__main__"):
    main()