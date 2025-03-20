import matplotlib.pyplot as plt
# read in data
grade_index = []
student_count = []

with open("grade_data.txt", 'r') as f:
    for line in f:
        line = line.split()
        grade_index.append(int(line[0]))
        student_count.append(int(line[1]))

print(student_count)

# calculate rainwater
leftIndex = 0
rightIndex = len(student_count) - 1
maxLeft = student_count[leftIndex]
maxRight = student_count[rightIndex]
total = 0
water_list = [-1 for a in grade_index]
water_list[0] = 0


# Solution
while leftIndex < rightIndex:
    if maxLeft < maxRight:
        leftIndex += 1
        maxLeft = max(maxLeft, student_count[leftIndex])
        water = maxLeft - student_count[leftIndex]
        total += water
        water_list[leftIndex] = water

    else:
        rightIndex -= 1
        maxRight = max(maxRight, student_count[rightIndex])
        water = maxRight - student_count[rightIndex]
        total += water
        water_list[rightIndex] = water
print(total)
print(water_list)

water_level = [a[0] + a[1] for a in zip(student_count, water_list)]
print(water_level)

plt.bar(grade_index, water_level, width=1.0, align="edge", color='#66b3ff', edgecolor='none', label="Water")
plt.bar(grade_index, student_count, width=1.0, align="edge", color='#2E2E2E', edgecolor='none', label="Students")

# scuffed fix
grade_index_plus_one = [a + 1 for a in grade_index]
plt.bar(grade_index_plus_one, water_level, width=1.0, align="edge", color='#66b3ff', edgecolor='none', label="Water")
plt.bar(grade_index_plus_one, student_count, width=1.0, align="edge", color='#2E2E2E', edgecolor='none', label="Students")


plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title("281 grade distro rainwater. Total: " + str(total), fontsize=14, fontweight='bold')
plt.xlabel("Grade", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xlim(min(grade_index), max(grade_index)+1)

plt.show()