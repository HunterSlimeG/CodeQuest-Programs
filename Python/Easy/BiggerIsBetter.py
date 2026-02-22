import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    nums = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    highest = nums[0]
    for n in nums:
        if n>highest:
            highest = n
    print(highest)