import re

with open('game.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Trouver les endif orphelins
if_count = 0
for i, line in enumerate(lines):
    if '{% if' in line:
        if_count += 1
    elif '{% endif' in line:
        if_count -= 1
        if if_count < 0:
            print("Line {}: ORPHAN endif found!".format(i+1))

# Nettoyer les doublons endif
cleaned_lines = []
last_was_endif = False
for line in lines:
    if '{% endif' in line:
        if not last_was_endif:
            cleaned_lines.append(line)
            last_was_endif = True
    else:
        cleaned_lines.append(line)
        last_was_endif = False

with open('game.html', 'w', encoding='utf-8') as f:
    f.writelines(cleaned_lines)

print("Cleaned!")
