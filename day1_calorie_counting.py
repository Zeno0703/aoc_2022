calories = open("C:\\Users\Zenov\Downloads\input.txt", "r")
calories_array = []
for calorie in calories:
    if (calorie.rstrip('\n')) == "":
        calories_array.append(calorie.rstrip('\n'))
    else:
        calories_array.append(int(calorie.rstrip('\n')))

cals_per_elf = []
cal_for_elf = []

for cal in calories_array:
    if cal != "":
        cal_for_elf.append(cal)
    else:
        sum_of_cals = 0
        for c in cal_for_elf:
            sum_of_cals += c
        cals_per_elf.append(sum_of_cals)
        cal_for_elf = []

print(cals_per_elf)
print(max(cals_per_elf))
print(cals_per_elf.index(max(cals_per_elf)))

counter = 1
summation = 0
while counter <= 3:
    maximum = max(cals_per_elf)
    summation += maximum
    cals_per_elf.remove(max(cals_per_elf))
    counter += 1

print(summation)