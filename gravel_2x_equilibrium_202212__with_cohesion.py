#! /usr/bin/python3

import ottar
import numpy as np
import importlib
importlib.reload(ottar)

# Time and discharge series
t = np.arange(0, 24*60.*60.*800, 24*60.*60./10.)
Q = 20.*np.ones(len(t))
Q[4000:] = 10.
Q[:2000] = 12.

#t = t[:2000]
#Q = Q[:2000]

# Gravel: ~1 Pa to initiate motion per mm
# So 10 cm gravel: 100 Pa
rw = ottar.RiverWidth(h_banks=1., S=1E-2, tau_crit=5, k_d=1E-7, k_E=0.01,
                                b0=4., f_stickiness=1E-2,
                                k_n_noncohesive=1E-5, D=0.06
                                )

# Simplified Minnesota River at Jordan / Belle Plaine, but because Manning's
# relationships don't vary *extraordinarily*, will hopefully be fine for an
# example.
rw.initialize_flow_calculations(0.03, 180, 1.5)

rw.initialize_timeseries(t,Q)
rw.run()
rw.finalize()
plt.ion()
rw.plotDischargeWidthWideningNarrowingGrainstressratio()
from matplotlib import pyplot as plt
plt.savefig('Width_Feedbacks_Response_Equilibrium.pdf')


