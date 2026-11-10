n, m, i = [int(j) for j in input().split(" ")]
nums = []
for mm in range(m):
    nums += [int(j) for j in input().split(" ")]
print(nums)

for ii in range(i):
    val = int(input())
    count = 0
    for num in nums:
        count += 1 if num >= val else 0
    print(count)