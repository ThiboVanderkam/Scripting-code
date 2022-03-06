import numpy as np
# list = [4, 5, 6, 7]
# array = np.array([4, 5, 6, 7])

# print(list * 2)
# print(array * 2)

# omzetKwartaal1 = np.array([3000, 4000, 5000])
# omzetKwartaal1InclBtw = omzetKwartaal1 * 1.21
# print(omzetKwartaal1InclBtw)

# kostenKwartaal1 = np.array([1500, 700, 0])
# winstKwartaal1 = omzetKwartaal1InclBtw - kostenKwartaal1
# print(winstKwartaal1)

# print(winstKwartaal1 > 2500)
# print(np.where(winstKwartaal1 > 2500))
# print(np.where(winstKwartaal1 > 2500, winstKwartaal1, 0))

# student1 = [16, 14, 12]
# student2 = [12, 14, 12]
# student3 = [10, 11, 14]

# gradebook = np.array([
#     [16, 14, 12],
#     [12, 14, 12],
#     [10, 11, 14]
# ])

# print(gradebook.sum(axis=1) / len(gradebook))
# print(gradebook.sum(axis=0) / len(gradebook))
# print(gradebook.min(axis=1))

# boekhouding = [ 1000, 2000, 3000, 500, 600, 800, 400, 250, 100, 100, 1000, 5000]
# boekhoudingNp = np.array(boekhouding)
# boekhoudingPerKwartaal = np.reshape(boekhoudingNp, (4, 3))
# print(boekhoudingPerKwartaal.sum(axis=1).max())

# list = np.array([4, 5, 6])
# print(list.dtype)
# listFloat = list.astype('str')
# print(listFloat)
# print(listFloat.dtype)

list = np.arange(10)
print(list[8:])
print(list[::-1])
