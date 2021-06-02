import matplotlib.pyplot as g
import numpy


# define
def b(l, l_0):
    return (29.0 / (l**2)) * ((l / l_0) - 1.0)


x_max = 3
l_0 = 1.24
l_1 = 0.62
l_2 = 0.496
l_3 = 0.413
l_4 = 0.354
l_5 = 0.31
l_6 = 0.248
x0 = numpy.arange(l_0, x_max, 0.01)
x1 = numpy.arange(l_1, x_max, 0.01)
x2 = numpy.arange(l_2, x_max, 0.01)
x3 = numpy.arange(l_3, x_max, 0.01)
x4 = numpy.arange(l_4, x_max, 0.01)
x5 = numpy.arange(l_5, x_max, 0.01)
x6 = numpy.arange(l_6, x_max, 0.01)
g.plot(x6, b(x6, l_6), label=r"$U_B = 50$ kV")
g.plot(x5, b(x5, l_5), label=r"$U_B = 40$ kV")
# g.plot(x4, b(x4, l_4), label=r"$U_B = 35$ kV")
g.plot(x3, b(x3, l_3), label=r"$U_B = 30$ kV")
# g.plot(x2, b(x2, l_2), label=r"$U_B = 25$ kV")
g.plot(x1, b(x1, l_1), label=r"$U_B = 20$ kV")
g.plot(x0, b(x0, l_0), label=r"$U_B = 10$ kV")
g.legend()
g.grid()
g.xlabel(r"Wellenlänge $\lambda$ in [Å]", fontsize=16)
g.ylabel(r"Intensität $I$ (a.u.)", fontsize=16)
g.savefig("plots/bremsstrahlung.png")
g.show()