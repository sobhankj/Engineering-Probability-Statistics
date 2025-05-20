import matplotlib.pyplot as plt
import numpy as np


x_asli = np.array([-2.3, -1.1, 0.5, 3.2, 4.0, 6.7, 10.3, 11.5])
y_asli = np.array([-9.6, -4.9, -4.1, 2.7, 5.9, 10.8, 18.9, 20.5])

### for 8 data asli
x = np.array(list(x_asli) + list(np.array([]))) 
y = np.array(list(y_asli) + list(np.array([])))
temp1 = np.sum(x*y)-len(x)*np.mean(x)*np.mean(y)
temp2 = np.sum(x*x)-len(x)*np.mean(x)*np.mean(x)
a = temp1 / temp2
print('a: ', a)
b = np.mean(y)-a*np.mean(x)
print('b: ', b)
Y = a * x + b
temp1 = (np.sum((y - Y)**2))
temp2 = (np.sum((y - np.mean(y))**2))
r2 = 1 - (temp1 / temp2)
print('r2: ', r2)
plt.scatter(x, y, color = "red")
plt.plot(x, Y)
plt.show()

### for 8 data asli + noghat dor oftadeh
# x = np.array(list(x_asli) + list(np.array([5.8]))) 
# y = np.array(list(y_asli) + list(np.array([31.3])))
# temp1 = np.sum(x*y)-len(x)*np.mean(x)*np.mean(y)
# temp2 = np.sum(x*x)-len(x)*np.mean(x)*np.mean(x)
# a = temp1 / temp2
# print('a: ', a)
# b = np.mean(y)-a*np.mean(x)
# print('b: ', b)
# Y = a * x + b
# temp1 = (np.sum((y - Y)**2))
# temp2 = (np.sum((y - np.mean(y))**2))
# r2 = 1 - (temp1 / temp2)
# print('r2: ', r2)
# plt.scatter(x, y, color = "red")
# plt.plot(x, Y)
# plt.show()

### for 8 data asli + noghat ahromi
# x = np.array(list(x_asli) + list(np.array([20.4]))) 
# y = np.array(list(y_asli) + list(np.array([14.1])))
# temp1 = np.sum(x*y)-len(x)*np.mean(x)*np.mean(y)
# temp2 = np.sum(x*x)-len(x)*np.mean(x)*np.mean(x)
# a = temp1 / temp2
# print('a: ', a)
# b = np.mean(y)-a*np.mean(x)
# print('b: ', b)
# Y = a * x + b
# temp1 = (np.sum((y - Y)**2))
# temp2 = (np.sum((y - np.mean(y))**2))
# r2 = 1 - (temp1 / temp2)
# print('r2: ', r2)
# plt.scatter(x, y, color = "red")
# plt.plot(x, Y)
# plt.show()


### for 8 data asli + nogaht dor oftadeh_ahromi
# x = np.array(list(x_asli) + list(np.array([20.4]))) 
# y = np.array(list(y_asli) + list(np.array([31.3])))
# temp1 = np.sum(x*y)-len(x)*np.mean(x)*np.mean(y)
# temp2 = np.sum(x*x)-len(x)*np.mean(x)*np.mean(x)
# a = temp1 / temp2
# print('a: ', a)
# b = np.mean(y)-a*np.mean(x)
# print('b: ', b)
# Y = a * x + b
# temp1 = (np.sum((y - Y)**2))
# temp2 = (np.sum((y - np.mean(y))**2))
# r2 = 1 - (temp1 / temp2)
# print('r2: ', r2)
# plt.scatter(x, y, color = "red")
# plt.plot(x, Y)
# plt.show()