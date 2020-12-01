def maxProduct(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n-1
    
    return 0