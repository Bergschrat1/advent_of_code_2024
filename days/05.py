from functools import cmp_to_key
from pathlib import Path
import numpy as np
import itertools

input_path = Path(__file__).parent.parent / "inputs" / Path(__file__).with_suffix(".txt").name
with open(input_path, "r") as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]
ans = 0

rules = [list(map(int, l.split("|"))) for l in lines if "|" in l]
updates = [list(map(int, l.split(","))) for l in lines if "|" not in l and l != ""]


def rule_sort(l, r):
    s = {l, r}
    for r in rules:
        if s.issubset(r):
            return -1 if r[0] == l else 1
    return 0


def is_sorted(l):
    return sorted(l, key=cmp_to_key(rule_sort)) == l


p2 = 0
for u in updates:
    if is_sorted(u):
        ans += u[int(len(u) / 2)]
    else:
        sorted_u = sorted(u, key=cmp_to_key(rule_sort))
        p2 += sorted_u[int(len(sorted_u) / 2)]
print(ans)
print(p2)
