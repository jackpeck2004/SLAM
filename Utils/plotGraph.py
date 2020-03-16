import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

p = [1,2,3,4,5,6]

for i in p:
    ax.scatter(i, i, i)

plt.show()

