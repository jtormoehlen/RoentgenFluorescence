import matplotlib.pyplot as g
import numpy


x, y = numpy.genfromtxt('spectra/snail.txt', delimiter='\t', unpack=True)[:,:-1]
g.plot(x,y)
# print(x)
# print(y)
g.xlabel(r"Energie $E$ in [keV]", fontsize=16)
g.ylabel(r"Intensität $I$ (a.u.)", fontsize=16)
g.grid()
g.text(3.69, 575, r"Ca$_{K_{\alpha}}$", fontsize=16)
g.text(4.01, 250, r"Ca$_{K_{\beta}}$", fontsize=16)
g.vlines(3.69, 0, 575, linestyle="dashed", colors="grey")
g.vlines(4.01, 0, 250, linestyle="dashed", colors="grey")
g.savefig("plots/snail.png")
g.show()
