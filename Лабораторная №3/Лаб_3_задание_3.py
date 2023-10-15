import re

with open('subj.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

subj_dict = {}
details = []

for line in lines:
    parts = line.strip().split(':')
    if len(parts) == 2:
        subj = parts[0] #predmet
        details = parts[1] #chasy

    num = re.findall(r'\d+', details)

    total = sum(map(int, num))
    subj_dict[subj] = total

print(subj_dict)
