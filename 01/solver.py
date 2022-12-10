# Day 1 Part 1
max_calories = 0
current_elf = []
for line in open("input.txt"):
    if not line.strip():
        calories = sum(current_elf)
        if calories > max_calories:
            max_calories = calories
        current_elf = []
    else:
        current_elf.append(int(line))


print(max_calories)


# Day 1 Part 2
all_elves_calories = []

current_elf = []
for line in open("input.txt"):
    if not line.strip():
        calories = sum(current_elf)
        all_elves_calories.append(calories)
        current_elf = []
    else:
        current_elf.append(int(line))

all_elves_calories = sorted(all_elves_calories, reverse=True)
top_three = all_elves_calories[0] + all_elves_calories[1] + all_elves_calories[2]
print(top_three)
