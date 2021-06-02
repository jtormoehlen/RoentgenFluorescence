import matplotlib.pyplot as g
import numpy


# define
def b(l, l_0):
    return (29.0 / (l**2)) * ((l / l_0) - 1.0)


def c(l, l_max, sigma, a):
    return (a / numpy.sqrt(2.0*numpy.pi*sigma**2)) * numpy.exp(-((l - l_max)**2 / (2.0 * sigma**2)))


x_max = 3
l_0 = 0.248
l_max1 = 1.543
l_max2 = 1.392
sigma = 0.01
x0 = numpy.arange(l_0, x_max, 0.01)
g.plot(x0, b(x0, l_0) + c(x0, l_max1, sigma, 5) + c(x0, l_max2, sigma, 2))
# g.plot(x0, c(x0, l_max, sigma))
g.grid()
g.xlabel(r"Wellenlänge $\lambda$ in [Å]", fontsize=16)
g.ylabel(r"Intensität $I$ (a.u.)", fontsize=16)
g.text(l_max1 + 0.05, 230, r"$K_\alpha$", fontsize=16)
g.text(l_max2 - 0.2, 135, r"$K_\beta$", fontsize=16)
g.savefig("plots/spektrum.png")
g.show()
