import matplotlib.pyplot as g
import numpy


x, y = numpy.genfromtxt('spectra/copper.txt', delimiter='\t', unpack=True)[:,:-1]
g.plot(x,y)
# print(x)
# print(y)
g.xlabel(r"Energie $E$ in [keV]", fontsize=16)
g.ylabel(r"Intensität $I$ (a.u.)", fontsize=16)
g.grid()
g.text(8.5, 1100, r"Cu$_{K_{\alpha}}$", fontsize=16)
g.text(9.25, 150, r"Cu$_{K_{\beta}}$", fontsize=16)
g.vlines(8.04, 0, 1100, linestyle="dashed", colors="grey")
g.vlines(8.91, 0, 150, linestyle="dashed", colors="grey")
g.savefig("plots/copper.png")
g.show()