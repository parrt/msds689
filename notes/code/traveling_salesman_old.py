# THIS TURNED INTO A JUNK DRAWER
import numpy as np
import matplotlib.pyplot as plt

class City:
    def __init__(self, name, x, y):
        self.name = name
        self.location = np.array([x, y])
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()
    def distance(self, other):
        return np.abs(np.linalg.norm(self.location - other.location))

n = 5
X = np.random.randint(0,100,n)
Y = np.random.randint(0,100,n)

names = ['SF', 'SEA', 'OAK', 'WASH', 'DALLAS', 'DENVER', 'LA']
cities = [City(names[i],x,y) for i,(x,y) in enumerate(zip(X,Y))]

A = City("A", 2, 0)
B = City("B", 0, 2)
print(A.distance(B))


# From https://nbviewer.jupyter.org/url/norvig.com/ipython/TSP.ipynb
def plot_tour(tour):
    "Plot the cities as circles and the tour as lines between them."
    plot_lines(list(tour) + [tour[0]])

# From https://nbviewer.jupyter.org/url/norvig.com/ipython/TSP.ipynb
def plot_lines(points, style='bo-'):
    "Plot lines to connect a series of points."
    plt.plot([p.location[0] for p in points], [p.location[1] for p in points], style)
    plt.axis('scaled')
    plt.axis('off')

plot_tour(cities)
plt.show()