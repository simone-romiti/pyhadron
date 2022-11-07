# Creating a cf_orig from a matrix

import numpy as np
import sys 
sys.path.append('../')

from pyhadron import Rwrap 
from Rwrap import hadron
from Rwrap import graphics

from pyhadron import from_R
from pyhadron import cf


time_extent = 96
e0_val = 0.12
e1_val = 0.0
rel_amplitude = 0.4
boot_R = 99
n_meas = 1000

np.random.seed(11631736)

a0_val = 1.0
a1_val = rel_amplitude
a0_err = 0.001
a1_err = 0.001
a0_gauss = np.random.normal(loc=a0_val, scale=a0_err, size=n_meas)
a1_gauss = np.random.normal(loc=a1_val, scale=a1_err, size=n_meas)
a0_orig = np.array([time_extent*[a0_gauss[i]] for i in range(n_meas)])
a1_orig = np.array([time_extent*[a1_gauss[i]] for i in range(n_meas)])

e0_err = 0.001
e1_err = 0.001
e0_gauss = np.random.normal(loc=e0_val, scale=e0_err, size=n_meas)
e1_gauss = np.random.normal(loc=e1_val, scale=e1_err, size=n_meas)
e0_orig = np.array([time_extent*[e0_gauss[i]] for i in range(n_meas)])
e1_orig = np.array([time_extent*[e1_gauss[i]] for i in range(n_meas)])

t = np.array([range(0, time_extent) for i in range(n_meas)])

signal_val = a0_val * (np.exp(-e0_val * t) + np.exp(-e0_val * (time_extent - t))) + a1_val * (np.exp(-e1_val * t) + np.exp(-e1_val * (time_extent - t)))
signal_orig = a0_orig * (np.exp(-e0_orig * t) + np.exp(-e0_orig * (time_extent - t))) + a1_orig * (np.exp(-e1_orig * t) + np.exp(-e1_orig * (time_extent - t)))

signal_err = np.std(signal_orig, axis=0)

hadron.plotwitherror(
     t, signal_val, signal_err,
     log = 'y',
     main = 'Artificial pure signal'
     )

input()

corr = cf.cf_orig(cf.cf_meta(Time = time_extent), _cf = signal_orig)
corr_boot = hadron.bootstrap_cf(hadron.symmetrise_cf(corr), boot_R = boot_R)

print("Attributes names of corr_boot:")
print(from_R.to_list(from_R.names(corr_boot)))

graphics.plot(corr_boot,
     log = 'y',
     main = 'Symmetrized correlator with noise')

input()

# effmass_solve <- bootstrap.effectivemass(corr_boot, type = 'solve')
# plot(effmass_solve, ylim = range(effmass_solve$t0, e0_val, na.rm = TRUE))
# abline(h = e0_val)

# corr_shifted <- takeTimeDiff.cf(corr_boot)
# effmass_shifted <- bootstrap.effectivemass(corr_shifted, type = 'shifted')
# plot(effmass_shifted)
# abline(h = e0_val)

# fit_single <- new_matrixfit(
#   corr_boot,
#   t1 = 1,
#   t2 = 47,
#   useCov = TRUE,
#   model = 'single',
#   fit.method = 'lm')

# plot(fit_single,
#      log = 'y',
#      main = 'Fit with “single” model')
# residual_plot(fit_single)

# fit_shifted <- new_matrixfit(
#   corr_shifted,
#   t1 = 1,
#   t2 = 47,
#   model = 'shifted',
#   useCov = TRUE,
#   fit.method = 'lm')

# plot(fit_shifted,
#      log = 'y',
#      main = 'Fit with “shifted” model')
# residual_plot(fit_shifted)

# fit_n_particle <- new_matrixfit(
#   corr_boot,
#   t1 = 1,
#   t2 = 47,
#   model = 'n_particles',
#   fit.method = 'lm',
#   useCov = TRUE,
#   higher_states = list(val = c(e1_val),
#                        ampl = c(1),
#                        boot = matrix(rnorm(boot_R, e1_val, e1_err / sqrt(n_meas)), ncol = 1)))

# plot(fit_n_particle,
#      log = 'y',
#      main = 'Fit with “n_particle” model')
# residual_plot(fit_n_particle)
