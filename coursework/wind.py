import numpy
from matplotlib import pyplot

x = numpy.linspace(0, 10, 80)
y = numpy.linspace(0, 1, 20)

X, Y = numpy.meshgrid(x, y)

U = 4*numpy.sin(2*numpy.pi*Y)*numpy.cos(numpy.pi*X/2)
V = -numpy.cos(2*numpy.pi*Y)*numpy.sin(numpy.pi*X/2)

fig = pyplot.figure(figsize=(10, 2), frameon=True)
ax = fig.add_subplot(1, 1, 1)
ax.quiver(X, Y, 0.25*U, V, numpy.sqrt(U**2 + V**2))
ax.set_ylabel("$y$", fontsize=14)
bbox_artists = [ax.set_xlabel("$x$", fontsize=14)]
fig.savefig("wind-field.pdf",
            orientation="landscape", format="pdf",
            transparent=True,
            bbox_inches="tight",
            bbox_extra_artists=bbox_artists)
