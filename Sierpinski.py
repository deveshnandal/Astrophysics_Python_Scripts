###############################################
######## Sierpinski's Tetrahedron #############
###############################################

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def sierpinski_3d(points, depth):
    if depth == 0:
        return [points]
    else:
        new_points = []
        for i in range(4):
            new_points += sierpinski_3d(points / 2 + points[i] / 2, depth - 1)
        return new_points

def plot_tetrahedron(ax, tetrahedron, color):
    faces = [
        [tetrahedron[0], tetrahedron[1], tetrahedron[2]],
        [tetrahedron[0], tetrahedron[1], tetrahedron[3]],
        [tetrahedron[0], tetrahedron[2], tetrahedron[3]],
        [tetrahedron[1], tetrahedron[2], tetrahedron[3]],
    ]
    poly = Poly3DCollection(faces, alpha=0.5)
    poly.set_facecolor(color)
    ax.add_collection3d(poly)

def main():
    # Define the 4 vertices of the initial tetrahedron
    tetrahedron_vertices = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0.5, np.sqrt(3) / 2, 0],
        [0.5, np.sqrt(3) / 6, np.sqrt(2 / 3)]
    ])

    depth = 4  # Number of recursive subdivisions

    # Generate the Sierpinski Tetrahedron points
    tetrahedra = sierpinski_3d(tetrahedron_vertices, depth)

    # Create a 3D plot of the tetrahedra
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for tetrahedron in tetrahedra:
        plot_tetrahedron(ax, tetrahedron, color='blue')

    # Set plot properties
    ax.set_title('3D Sierpinski Tetrahedron')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.view_init(elev=20, azim=120)

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()

##############################################
### Barnsley's Fern ##########################
##############################################

import numpy as np
import matplotlib.pyplot as plt

def barnsley_fern(n):
    x, y = 0, 0
    xs, ys = [x], [y]

    for _ in range(n):
        r = np.random.random()
        if r < 0.01:
            x, y = 0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        xs.append(x)
        ys.append(y)

    return xs, ys

def main():
    n = 100000  # Number of iterations
    xs, ys = barnsley_fern(n)

    plt.figure(figsize=(6, 10))
    plt.scatter(xs, ys, color='green', marker='.', s=1)
    plt.title('Barnsley Fern')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()


#########################################
####### Animated Barnsley's fern ########
#########################################

import matplotlib
matplotlib.use('Qt5Agg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def barnsley_fern_point(x, y):
    r = np.random.random()
    if r < 0.01:
        x, y = 0, 0.16 * y
    elif r < 0.86:
        x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
    elif r < 0.93:
        x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    else:
        x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
    return x, y

def update(frame, x, y, scat):
    x_new, y_new = barnsley_fern_point(x[-1], y[-1])
    x.append(x_new)
    y.append(y_new)
    scat.set_offsets(np.c_[x, y])

    return scat,

def main():
    n = 10000  # Number of iterations

    x, y = [0], [0]
    fig, ax = plt.subplots(figsize=(6, 10))
    scat = ax.scatter(x, y, color='green', marker='.', s=1)
    ax.set_title('Barnsley Fern')
    ax.axis('off')

    ani = FuncAnimation(fig, update, frames=range(n), fargs=(x, y, scat), interval=1, blit=True, repeat=False)
    plt.show()

if __name__ == "__main__":
    main()
