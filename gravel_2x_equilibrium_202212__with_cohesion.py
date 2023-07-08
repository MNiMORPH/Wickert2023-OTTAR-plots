#! /usr/bin/python3

import ottar
import numpy as np
import importlib
importlib.reload(ottar)
from matplotlib import pyplot as plt

# Time and discharge series
ndays = 500
t = np.arange(0, 24*60.*60.*ndays, 24*60.*60./10.)
Q = 20.*np.ones(len(t))
Q[2000:] = 10.
Q[:1000] = 12.

#t = t[:2000]
#Q = Q[:2000]

# Gravel: ~1 Pa to initiate motion per mm
# So 10 cm gravel: 100 Pa
rw = ottar.RiverWidth(h_banks=1., S=1E-2, tau_crit=5, k_d=1E-3, k_E=8E-3,
                                b0=4., f_stickiness=5E-3,
                                k_n_noncohesive=5E-3, D=0.06
                                )
self = rw

# Simplified Minnesota River at Jordan / Belle Plaine, but because Manning's
# relationships don't vary *extraordinarily*, will hopefully be fine for an
# example.
#rw.initialize_flow_calculations(0.03, 180, 1.5, use_Rh=False)
rw.initialize_flow_calculations(0.025, 100, 1.75, use_Rh=True)


rw.initialize_timeseries(t,Q)
rw.run()
rw.finalize()
plt.ion()
rw.plotDischargeWidthWideningNarrowingGrainstressratio()
plt.show()
plt.savefig('Width_Feedbacks_Response_Equilibrium.pdf')

