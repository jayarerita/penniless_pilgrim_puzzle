
for y in range(4, -1, -1):
    line = []
    for x in range(5):
        line.append('('+str(x)+str(y)+')')
    print(line)

for y in range(4, -1, -1):
    line = ''
    for x in range(5):
        if x != 4:
            section = '('+str(x)+str(y)+')-'
        else:
            section = '('+str(x)+str(y)+')'
        line += section
    print(line)
    if y != 0:
        print(' |     |    |    |    |')

street = '4 to 3'
print(street.split(" "))

valid = ['E', "W", "N"]
exclude = ["N"]
valid = [x for x in valid if x not in exclude]
print(valid)
