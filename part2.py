import numpy as np
import matplotlib.pyplot as plt
import csv

x = np.arange(0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)
a = np.tan(x)

plt.subplot(221)
plt.plot(y)
plt.subplot(222)
plt.plot(z)
plt.subplot(223)
plt.plot(a)
plt.subplot(224)
plt.plot(x)
plt.show()

plt.plot(x, y, 'k', linewidth=4)
plt.plot(x, z, 'g', linewidth=2)
plt.plot(x, a, 'ro', linewidth=4, markersize=3)
plt.plot(x, x, 'b', linewidth=2)
plt.show()

csvfile = open('Temperature.csv', 'r')
reader = csv.reader(csvfile)
data = [data for data in reader]
data_array = np.asarray(data)
data_array = np.delete(data_array, (0), axis=0)

plt.title('Day vs. Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.plot(data_array[:,0], data_array[:,1])
plt.show()
