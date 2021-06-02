import matplotlib.pyplot as g
import numpy


x1, y1 = numpy.genfromtxt('spectra/ring.txt', delimiter='\t', unpack=True)[:,:-1]
x2, y2 = numpy.genfromtxt('spectra/case.txt', delimiter='\t', unpack=True)[:,:-1]

y3 = y1 - y2
for i in range(len(y3)):
    if y3[i] < 0:
        y3[i] = 0

ag_l_alpha = 2.98
ag_l_beta = 3.15
fe_k_alpha = 6.4
cu_k_alpha = 8.04
zn_k_alpha = 8.64
zn_k_beta = 9.57

print(y3)
g.plot(x1, y3)
# print(x)
# print(y)
g.xlabel(r"Energie $E$ in [keV]", fontsize=16)
g.ylabel(r"Intensität $I$ (a.u.)", fontsize=16)
g.grid()
# g.text(ag_l_alpha, 150, r"Ag$_{L_{\alpha}}$", fontsize=16)
g.text(ag_l_beta, 150, r"Ag$_{L_{\beta}}$", fontsize=16)
# g.text(fe_k_alpha, 150, r"Fe$_{K_{\alpha}}$", fontsize=16)
g.text(cu_k_alpha - 1.5, 150, r"Cu$_{K_{\alpha}}$", fontsize=16)
g.text(zn_k_alpha, 150, r"Zn$_{K_{\alpha}}$", fontsize=16)
# g.text(zn_k_beta, 150, r"Zn$_{K_{\beta}}$", fontsize=16)
# g.vlines(ag_l_alpha - 1, 0, 150, linestyle="dashed", colors="grey")
g.vlines(ag_l_beta, 0, 150, linestyle="dashed", colors="grey")
# g.vlines(fe_k_alpha, 0, 150, linestyle="dashed", colors="grey")
g.vlines(cu_k_alpha, 0, 150, linestyle="dashed", colors="grey")
g.vlines(zn_k_alpha, 0, 150, linestyle="dashed", colors="grey")
# g.vlines(zn_k_beta, 0, 150, linestyle="dashed", colors="grey")
g.savefig("plots/ring.png")
g.show()
