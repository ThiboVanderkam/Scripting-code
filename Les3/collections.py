def studentAverage(student):
    sum = 0
    for element in student:
        sum += element
    return str(sum / len(student))

def testAverage(testnum):
    index = testnum - 1
    sum = 0
    for element in students:
        sum += element[index]
    return str(sum / len(students))

student1 = [16, 14, 12]
student2 = [12, 14, 12]
student3 = [10, 11, 14]

students = [student1, student2, student3]

print("\nStudent Average:")
print("\t" + studentAverage(student1))
print("\t" + studentAverage(student2))
print("\t" + studentAverage(student3))
print("--------------------------")
print("Test Average:")
print("\t" + testAverage(1))
print("\t" + testAverage(2))
print("\t" + testAverage(3))