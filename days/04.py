from pathlib import Path
import numpy as np
import itertools

input_path = Path(__file__).parent.parent / "inputs" / Path(__file__).with_suffix(".txt").name
with open(input_path, "r") as f:
    lines = f.readlines()

lines = [list(l.strip()) for l in lines]
a = np.array(lines)
ans = 0


def count_xmas(lines, target="XMAS"):
    count = 0
    for l in lines:
        line_str = "".join(l)
        count += line_str.count(target)
        count += line_str[::-1].count(target)
    return count


ans += count_xmas(a)
ans += count_xmas(np.transpose(a))

diags = []
diags_t = []
for i in range(-len(a), len(a)):
    diags.append(np.diagonal(a, i))
    diags_t.append(np.diagonal(np.flip(a, axis=1), i))

ans += count_xmas(diags)
ans += count_xmas(diags_t)
print(ans)

ans = 0
for x, y in itertools.product(range(a.shape[0] - 2), range(a.shape[1] - 2)):
    window = a[x : x + 3, y : y + 3]
    x_mas = bool(count_xmas([np.diagonal(window)], target="MAS")) and bool(count_xmas([np.diagonal(np.flip(window, axis=1))], target="MAS"))
    if x_mas:
        ans += 1
print(ans)
