content = open('game.html', 'r', encoding='utf-8').read()
lines = content.split('\n')

if_count = 0
for i, line in enumerate(lines, 1):
    if '{% if' in line:
        if_count += 1
        print("Line {}: IF #{} - {}".format(i, if_count, line.strip()[:80]))
    elif '{% endif' in line:
        if_count -= 1
        print("Line {}: ENDIF - {} (count now: {})".format(i, line.strip()[:80], if_count))
    elif '{% else' in line:
        print("Line {}: ELSE - {}".format(i, line.strip()[:80]))

print("\nFinal count: {} (should be 0)".format(if_count))
