def palindromes(s: str) -> int:
    if s is None:
        return 0
    if len(s) == 1:
        return 1

    centerRight = len(s) // 2
    centerLeft = centerRight-1
    p = len(s)
   
    while centerRight != len(s):
        if s[centerRight] == s[centerLeft]:
            p += 1
            if centerRight == len(s)-1 and len(s)%2 != 0:
                p += 1
        if centerLeft != 0:
            centerLeft -= 1
        centerRight += 1
        
    return p

def main():
    print(palindromes("abc")) # 3
    print(palindromes("aaa")) # 6
    print(palindromes("nellen")) # 9

if __name__==("__main__"):
    main()