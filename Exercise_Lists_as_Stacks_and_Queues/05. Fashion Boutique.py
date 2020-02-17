

clothes = [int(x) for x in input().split()]

capacity = int(input())

number_of_rack = 1
sums = 0
while clothes:
    current = clothes.pop()
    sums += current
    if sums<= capacity:
        pass
    else:
        clothes.append(current)
        number_of_rack+=1
        sums=0

print(number_of_rack)