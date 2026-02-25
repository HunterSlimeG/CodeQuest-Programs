import sys
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    nums = [int(i) for i in sys.stdin.readline().rstrip().split(",")]
    nums.sort()
    nums = [str(i) for i in nums]
    print(",".join(nums))
