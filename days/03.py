from pathlib import Path
import re

input_path = Path(__file__).parent.parent / "inputs" / Path(__file__).with_suffix(".txt").name
with open(input_path, "r") as f:
    lines = f.readlines()

ans = 0
data = "".join(lines)
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.finditer(pattern, data, re.MULTILINE)

for m in matches:
    a, b = map(int, m.groups())
    ans += a*b

print(ans)

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
matches = re.finditer(pattern, data, re.MULTILINE)
mul = True
ans = 0

for m in matches:
    match m.group(0):
        case "do()":
            mul = True
        case "don't()":
            mul = False
        case _:
            if mul:
                a, b = map(int, m.groups())
                ans += a*b
print(ans)
