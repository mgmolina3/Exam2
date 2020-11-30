def arithmeticSlices(A: list) -> int:
    if len(A) < 3:
        return 0
    if len(A) == 3:
        return 1 if A[1] - A[0] == A[2] - A[1] else 0
    i = 1
    x = 3
    d = {}
    d[0] = 1 if A[1] - A[0] == A[2] - A[1] else 0
    slices = d[0]
    while x < len(A):
        if A[x] - A[i+1] == A[i+1] - A[i]:
            d[i] = 1 + d.get(i-1, 0)
            slices = slices + d[i]
        x += 1
        i += 1
    return slices

def main():
    print(arithmeticSlices([1,2,3,4])) # 3
    print(arithmeticSlices([1,2,3,4,5])) # 6
    print(arithmeticSlices([1,2,3,4,5,6])) # 10

    print(arithmeticSlices([1,2,3,5,5,6])) # 1
    print(arithmeticSlices([3,3,3,3])) # 3
    print(arithmeticSlices([1,2,3,10,1,2,3])) # 2
    print(arithmeticSlices([1,3,5,7,9,15,20,25,28,29])) # 7
    
if __name__==("__main__"):
    main()