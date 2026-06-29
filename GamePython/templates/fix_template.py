import re

with open('game.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

if_stack = []
missing_endif_count = 0

for i, line in enumerate(lines, 1):
    if '{% if' in line:
        match = re.search(r'{%\s*if\s+([^%]+)%}', line)
        cond = match.group(1).strip()[:40] if match else '?'
        if_stack.append((i, cond))
    elif '{% elif' in line:
        pass
    elif '{% else' in line:
        pass
    elif '{% endif' in line:
        if if_stack:
            if_stack.pop()
        else:
            print("Orphan endif at line {}".format(i))

if if_stack:
    print("\nUnclosed IFs that need endif:")
    for line_num, cond in if_stack:
        print("  Line {}: {}".format(line_num, cond))
    print("\nNeed to add {} endif at the end".format(len(if_stack)))
else:
    print("All IFs are properly closed!")
