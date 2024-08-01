lines = 0
done = 0
ignored = 0

for line in open('README.md', 'r'):
    if len(line) < 4 or line[3] != '.':
        continue

    lines += 1

    if line[5] == '✅':
        done += 1

    if line[5] == '❎':
        ignored += 1

print('Lines:', lines)
print('Done:', done, '(' + str(done/lines * 100) + '%)')
print('Ignored:', ignored, '(' + str(ignored/lines * 100) + '%)')
print('Completed:', done + ignored, '(' + str(done + ignored/lines * 100) + '%)')
