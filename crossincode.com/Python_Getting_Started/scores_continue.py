f = file('scores.txt')
lines = f.readlines()
f.close()

results = []

for line in lines:
    data = line.split()

    sum = 0
    for score in data[1:]:
        point = int(score)
        if point < 60:
            continue
        sum += point
    result = '%s \t: %d\n' % (data[0], sum)

    results.append(result)

output = file('result.txt', 'w')
output.writelines(results)
output.close()
