import numpy as np
import pandas as pd
from pathlib import Path

input_path = Path(__file__).parent.parent / "inputs" / Path(__file__).with_suffix(".txt").name
with open(input_path, "r") as f:
    lines = f.readlines()

num_l = []
num_r = []

for l in lines:
    left, right = l.split()
    num_l.append(int(left))
    num_r.append(int(right))
arr_l = np.array(num_l)
arr_r = np.array(num_r)

p2 = 0
unique, counts = np.unique_counts(arr_r)
value_counts = dict(zip(unique, counts))
for l in arr_l:
    p2 += l * value_counts.get(l, 0)

arr_l = np.sort(arr_l)
arr_r = np.sort(arr_r)

diff = np.abs(arr_l-arr_r)
print("Part 1: ", diff.sum())
print("Part 2: ", p2)


