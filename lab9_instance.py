from lab9_class import my_stat
import numpy as np


my_cal = my_stat()

result1 = my_cal.cal_sigma(3, 5)
print("Sigma(3,5) = ", result1)

result2 = my_cal.pi(3, 5)
print("Pi(3,5) = ", result2)

result3 = my_cal.factorial(5)
print("Factorial(5) = ", result3)

result4 = my_cal.permutation(2, 5)
print("Permutation(2,5) = ", result4)

print(np.math.factorial(999))
print(my_cal.factorial(999))

