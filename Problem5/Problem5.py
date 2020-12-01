def longestChain(nums: list) -> int:
    if len(nums) == 1:
        return 1
    nums.sort()
    chains = [1] * len(nums)
    maxChain = 1

    for x in range(1, len(nums)):
        for y in range(x):
            if nums[y][1] < nums[x][0]:
                chains[x] = max(chains[y]+1, maxChain)
                maxChain = chains[x]
    
    return maxChain

def main():
    print(longestChain([[1,2],[2,3],[3,4]])) # 2
    print(longestChain([[1,2],[3,4],[4,5],[5,6]])) # 3
    print(longestChain([[1,2],[2,3],[4,5],[6,7]])) # 3
    print(longestChain([[1,5],[2,3],[4,5],[6,7]])) # 3
    print(longestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]])) # 3
    
if __name__==("__main__"):
    main()