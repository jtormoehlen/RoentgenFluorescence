import matplotlib.pyplot as g
import numpy


x, y = numpy.genfromtxt('spectra/buck.txt', delimiter='\t', unpack=True)[:,:-1]
g.plot(x,y)
cu_k_alpha = 8.04
cu_k_beta = 8.91
zn_k_alpha = 8.64
zn_k_beta = 9.57
mn_k_alpha = 5.9
mn_k_beta = 6.49
g.xlabel(r"Energie $E$ in [keV]", fontsize=16)
g.ylabel(r"Intensität $I$ (a.u.)", fontsize=16)
g.grid()
g.text(mn_k_alpha - 1.75, 100, r"Mn$_{K_{\alpha}}$", fontsize=16)
g.text(mn_k_beta - 0.75, 100, r"Mn$_{K_{\beta}}$", fontsize=16)
g.text(cu_k_alpha, 1450, r"Cu$_{K_{\alpha}}$", fontsize=16)
g# .text(cu_k_beta, 200, r"Cu$_{K_{\beta}}$", fontsize=16)
g.text(zn_k_alpha, 375, r"Zn$_{K_{\alpha}}$", fontsize=16)
# g.text(zn_k_beta, 150, r"Zn$_{K_{\beta}}$", fontsize=16)
g.vlines(mn_k_alpha, 0, 75, linestyle="dashed", colors="grey")
g.vlines(mn_k_beta, 0, 30, linestyle="dashed", colors="grey")
g.vlines(cu_k_alpha, 0, 1450, linestyle="dashed", colors="grey")
# g.vlines(cu_k_beta, 0, 150, linestyle="dashed", colors="grey")
g.vlines(zn_k_alpha, 0, 350, linestyle="dashed", colors="grey")
# g.vlines(zn_k_beta, 0, 150, linestyle="dashed", colors="grey")
g.savefig("plots/buck.png")
g.show()
