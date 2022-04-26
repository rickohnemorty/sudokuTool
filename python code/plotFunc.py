import numpy as np
from matplotlib import pyplot as plt


# matrix to array of average values
def matrix_to_avgval_array(matrix):
    result = []
    for i in matrix:
        result.append(sum(i)/9)
    return result


# scatter3D plot of all zeros with values on the z-axe
def plot_zero_values(input):
    plot1 = plt.figure(1)
    y = input[0]
    x = input[1]
    Value = input[2]

    y = np.asarray(y[::-1])
    x = np.asarray(x)
    z = np.asarray(Value[::-1])
    zmin = np.min(z)
    mask = np.array(z) == zmin
    color = np.where(mask, 'red', 'blue')

    plt.rcParams['figure.figsize'] = (9, 9)

    ax = plt.axes(projection='3d')
    ax.scatter3D(x, y, z, s=100, color=color)
    plt.title('gaps ranked by difficulty')
    ax.set_xlabel('column')
    ax.set_ylabel('row')
    ax.set_zlabel('value')


# bar2D plot for the rows
def plot_rows_avgvalue(input):
    plot2 = plt.figure(2)
    y = input[1]
    z = matrix_to_avgval_array(input[0])
    zmin = np.min(z)
    mask = np.array(z) == zmin
    color = np.where(mask, 'red', 'blue')
    plt.bar(y, z, color=color, width=0.4)
    plt.xlabel("rows")
    plt.ylabel("avg. value")
    plt.title("rows ranked by difficulty")



