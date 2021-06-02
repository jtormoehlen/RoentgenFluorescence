import matplotlib.pyplot as g
import numpy


def c(l, l_max, sigma, peak):
    return (peak / numpy.sqrt(2.0*numpy.pi*sigma**2)) * numpy.exp(-((l - l_max)**2 / (2.0 * sigma**2)))


x, y = numpy.genfromtxt('spectra/wolfram.txt', delimiter='\t', unpack=True)[:,:-1]
l_alpha_1 = 8.397
l_alpha_2 = 8.335
l_alpha_mean = numpy.mean([l_alpha_1, l_alpha_2], dtype=numpy.float64)
l_beta_1 = 9.673
l_beta_2 = 9.961
l_beta_3 = 9.818
l_beta_4 = 9.525
l_beta_5 = 10.200
l_beta_6 = 9.611
l_beta_mean = numpy.mean([l_beta_1, l_beta_2, l_beta_3, l_beta_4, l_beta_5, l_beta_6], dtype=numpy.float64)
l_gamma_l = 7.387
l_gamma_n = 8.725
l_gamma_1 = 11.286
l_gamma_2 = 11.608
l_gamma_3 = 11.674
l_gamma_4 = 12.063
l_gamma_mean = numpy.mean([l_gamma_1, l_gamma_2, l_gamma_3, l_gamma_4], dtype=numpy.float64)
sigma = 0.10
alt = numpy.arange(0.01, 15.00, 0.01)

# f, axarr = g.subplots(2, sharex=True)
# axarr[0].plot(alt, c(alt, l_alpha_mean, sigma, 10.0) + c(alt, l_beta_mean, sigma, 7.5) + c(alt, l_gamma_mean, sigma, 5.0))
# axarr[0].grid()
# axarr[1].plot(x, y)
# axarr[1].grid()
g.plot(x, y)
g.grid()
g.xlabel(r"Energie $E$ in [keV]", fontsize=16)
g.ylabel(r"Intensität $I$ (a.u.)", fontsize=16)
g.text(l_gamma_l - 0.5, 50, r"W$_{L_l}$", fontsize=16)
g.text(l_alpha_mean, 525, r"W$_{L_{\alpha}}$", fontsize=16)
g.text(l_beta_mean, 450, r"W$_{L_{\beta}}$", fontsize=16)
g.text(l_gamma_1, 40, r"W$_{L_{\gamma}}$", fontsize=16)
g.vlines(l_gamma_l, 0, 50, linestyle="dashed", colors="grey")
g.vlines(l_gamma_2, 0, 25, linestyle="dashed", colors="grey")
g.vlines(l_alpha_mean, 0, 525, linestyle="dashed", colors="grey")
g.vlines(l_beta_mean, 0, 450, linestyle="dashed", colors="grey")
g.vlines(l_gamma_1, 0, 40, linestyle="dashed", colors="grey")
g.savefig("plots/wolfram.png")
g.show()
