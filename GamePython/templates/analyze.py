import re

with open('game.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

if_stack = []
for i, line in enumerate(lines, 1):
    if '{% if' in line:
        match = re.search(r'{%\s*if\s+([^%]+)%}', line)
        cond = match.group(1).strip()[:50] if match else '?'
        if_stack.append((i, cond))
        print("Line {}: IF #{} - {}".format(i, len(if_stack), cond))
    elif '{% elif' in line:
        print("Line {}: ELIF".format(i))
    elif '{% else' in line:
        print("Line {}: ELSE".format(i))
    elif '{% endif' in line:
        if if_stack:
            line_num, cond = if_stack.pop()
            print("Line {}: ENDIF (closes line {} - {})".format(i, line_num, cond))
        else:
            print("Line {}: ENDIF (orphan!)".format(i))

print("\n=== UNCLOSED IFS ===")
for line_num, cond in if_stack:
    print("Line {}: {}".format(line_num, cond))
