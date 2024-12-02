from aocd import data
import itertools

lines = data.split("\n")
save = 0

for l in lines:
    nums = list(map(int, l.split()))
    decreasing = nums == sorted(nums)
    increasing = nums == sorted(nums, reverse=True)
    diff_good = all(0 < abs(l-r) <= 3 for l, r in itertools.pairwise(nums))
    if (decreasing or increasing) and diff_good:
        save += 1

print(save)

save = 0
for l in lines:
    nums = list(map(int, l.split()))
    for i in range(len(nums)):
        n = nums.copy()
        del n[i]
        decreasing = n == sorted(n)
        increasing = n == sorted(n, reverse=True)
        diff_good = all(0 < abs(l-r) <= 3 for l, r in itertools.pairwise(n))
        if (decreasing or increasing) and diff_good:
            save += 1
            break

print(save)