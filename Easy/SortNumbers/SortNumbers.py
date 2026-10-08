
cases = int(input())
for caseNum in range(cases):
    nums = [int(i) for i in input().split(",")]
    nums.sort()
    nums = [str(i) for i in nums]
    print(",".join(nums))
