# exponential fit

import numpy as np
import sys 
sys.path.append('../')


import pyhadron.Rhadron as hadron
import pyhadron.convert.from_R as from_R
import pyhadron.convert.from_python as from_python

import matplotlib.pyplot as plt

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

# plot signal_orig here!

corr = hadron.cf_orig(hadron.cf_meta(Time = time_extent), cf = signal_orig)
corr_boot = hadron.bootstrap_cf(hadron.symmetrise_cf(corr), boot_R = boot_R)

print("Attributes names of corr_boot:")

# plot corr_boot here

effmass_solve = hadron.bootstrap_effectivemass(corr_boot, type = 'solve')


E_i = from_R.to_numpy(from_R.get(effmass_solve, "effMass"))
dE_i = from_R.to_numpy(from_R.get(effmass_solve, "deffMass"))
t_i = np.array(range(0, len(E_i)))
plt.errorbar(t_i, E_i, yerr=dE_i, marker=".", linestyle="None")
#plt.show()

corr_shifted = hadron.takeTimeDiff_cf(corr_boot)
effmass_shifted = hadron.bootstrap_effectivemass(corr_shifted, type = 'shifted')

# plot effmass_shifted here!

fit_single = hadron.new_matrixfit(
  corr_boot,
  t1 = 1,
  t2 = 47,
  useCov = False,
  model = 'single',
  fit_method = 'lm')

# plot fit_single here!


fit_shifted = hadron.new_matrixfit(
  corr_shifted,
  t1 = 1,
  t2 = 47,
  model = 'shifted',
  useCov = False,
  fit_method = 'lm')

# plot fit_shifted here!

# boot_1 = np.random.normal(e1_val, e1_err / np.sqrt(n_meas), boot_R)
# hs_boot = np.array([[boot_1[i] for j in range(time_extent)] for i in range(boot_R)])

# hs = from_python.to_R_list({
#      "val": np.full((time_extent), e1_val), 
#      "ampl": np.full((time_extent), 1), 
#      "boot" : hs_boot}
#      )

# fit_n_particle = hadron.new_matrixfit(
#   corr_boot,
#   t1 = 10,
#   t2 = 20,
#   model = 'n_particles',
#   fit_method = 'lm',
#   useCov = False,
#   higher_states = hs)

# # plot fit_n_particle here!
