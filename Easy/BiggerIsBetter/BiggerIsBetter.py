
cases = int(input())
for caseNum in range(cases):
    nums = [int(i) for i in input().split(" ")]
    highest = nums[0]
    for n in nums:
        if n>highest:
            highest = n
    print(highest)