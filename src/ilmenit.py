import matplotlib.pyplot as g
import numpy


def c(l, l_max, sigma, peak):
    return (peak / numpy.sqrt(2.0*numpy.pi*sigma**2)) * numpy.exp(-((l - l_max)**2 / (2.0 * sigma**2)))


x, y = numpy.genfromtxt('spectra/ilmenit.txt', delimiter='\t', unpack=True)[:,:-1]
fe_k_alpha = 6.4
fe_k_beta = 7.058
ti_k_alpha = 4.51
ti_k_beta = 4.93
sigma = 0.10
alt = numpy.arange(0.01, 15.00, 0.01)

# f, axarr = g.subplots(2, sharex=True)
# axarr[0].plot(alt, c(alt, fe_k_alpha, sigma, 1.0) + c(alt, fe_k_beta, sigma, 1.0) + c(alt, ti_k_alpha, sigma, 1.0) + c(alt, ti_k_beta, sigma, 1.0))
# axarr[0].grid()
# axarr[1].plot(x, y)
# axarr[1].grid()
g.grid()
g.plot(x, y)
g.xlabel(r"Energie $E$ in [keV]", fontsize=16)
g.ylabel(r"Intensität $I$ (a.u.)", fontsize=16)
g.text(4.5, 150, r"Ti$_{K_{\alpha}}$", fontsize=16)
g.text(4.93, 75, r"Ti$_{K_{\beta}}$", fontsize=16)
g.text(6.5, 850, r"Fe$_{K_{\alpha}}$", fontsize=16)
g.text(7.25, 150, r"Fe$_{K_{\beta}}$", fontsize=16)
g.vlines(4.51, 0, 150, linestyle="dashed", colors="grey")
g.vlines(4.93, 0, 50, linestyle="dashed", colors="grey")
g.vlines(6.4, 0, 850, linestyle="dashed", colors="grey")
g.vlines(7.06, 0, 150, linestyle="dashed", colors="grey")
g.savefig("plots/ilmenit.png")
g.show()
