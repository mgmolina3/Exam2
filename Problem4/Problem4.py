def minASCIIsum(s1, s2) -> int:
    if s1 is None:
        minSum = 0
        for c in s2:
            minSum = minSum + ord(c)
        return minSum
    if s2 is None:
        minSum = 0
        for c in s1:
            minSum = minSum + ord(c)
        return minSum

    matrix = [[-1 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
    matrix[0][0] = 0

    for i in range(1, len(matrix[0])):
        matrix[0][i] = ord(s1[i-1]) + matrix[0][i-1]
    for i in range(1, len(s2)+1):
        matrix[i][0] = ord(s2[i-1]) + matrix[i-1][0]
    
    for y in range(1, len(s2)+1):
        for x in range(1, len(s1)+1):
            if s1[x-1] == s2[y-1]:
                matrix[y][x] = matrix[y-1][x-1]
            else:
                matrix[y][x] = min(matrix[y][x-1]+ord(s1[x-1]), matrix[y-1][x]+ord(s2[y-1]))
            
    return matrix[-1][-1]

def main():
    print(minASCIIsum("sea", "eat")) # 231
    print(minASCIIsum("delete", "leet")) # 403
    print(minASCIIsum("map", "hat")) # 441
    
if __name__==("__main__"):
    main()