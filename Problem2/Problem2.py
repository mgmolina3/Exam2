def palindromes(s: str) -> int:
    d = dict()
    p = len(s)
    i = 2
    while len(s) != 1:
        while i <= len(s):
            sub = s[0:i]
            if sub in d:
                p += 1 if d[sub] else 0
            else:
                p += 1 if isPalindrome(s) else 0
                d[sub] = isPalindrome(s)
            i += 1
        s = s[1:]
        i = 2
    return p

def isPalindrome(s: str) -> bool:
    return s == s[::-1]

def main():
    print(palindromes("abc")) # 3
    print(palindromes("aaa")) # 6
    print(palindromes("nellen")) # 6

if __name__==("__main__"):
    main()