import re

file = open('regex_sum_310803.txt')
i = 0
_sum = 0
count = 0

for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if(len(numbers) != 0):
        #print(numbers)
        for j in range(len(numbers)):
            _sum = _sum + int(numbers[j])
            count = count + 1
        #print (_sum)
        i = i + 1
    i = 0

print (count)
print (_sum)
