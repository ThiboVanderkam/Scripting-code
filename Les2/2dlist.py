def averagePerStudent(gradebook, i):
    total = 0
    for grade in gradebook[i]:
        total += grade
    
    average = total / len(gradebook[0])
    return average


gradebook = [
    [18, 20, 10, 14], # student1
    [10, 10, 10, 10]  # student2
]

totalAverage = 0

for i in range(0, len(gradebook)):
    av = averagePerStudent(gradebook, i)
    print("Average student", i+1, ":", av)
    totalAverage += av

totalAverage /= len(gradebook)
print("Total average is:", totalAverage)