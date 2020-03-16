import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotGraph(xArr, yArr, frameCount):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    frameCounter = []
    
    for i in range(frameCount):
        frameCounter.append(i)

    for x,y,z in zip(xArr, yArr, frameCounter):
        ax.scatter(x, z, y)

    plt.show()

    # print(frameCounter)

