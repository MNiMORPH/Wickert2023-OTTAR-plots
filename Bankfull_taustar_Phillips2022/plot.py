import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import lognorm, gamma

plt.ion()

df = pd.read_excel('Alluvial_river_bankfull_geometry__Phillips2022.xlsx')

"""
taustar = df['tau_*bf'][ np.isfinite(df['tau_*bf']) ]
loghist = np.histogram(np.log10(taustar), 100)
linhist = np.histogram(taustar, 100)

_y = loghist[0] / 100#np.sum(loghist[0]) # fraction
_logx = ( loghist[1][1:] + loghist[1][:-1] ) / 2.
_x = 10**_logx

_ylin = linhist[0]/100.
_xlin = ( linhist[1][1:] + linhist[1][:-1] ) / 2.

#plt.semilogx(_x, _y, 'k.')

#_shape, _loc, _scale = lognorm.fit(taustar, floc=0)
_shape, _loc, _scale = lognorm.fit(taustar, loc=1.2)

# Does the same thing as the below fcn -- keeping for learning + reference
#_lognorm = lognorm(_shape, _loc, _scale)
#_pdf = _lognorm.pdf(_x)

_pdf = lognorm.pdf(_x, _shape, _loc, _scale)

plt.semilogx(_xlin, _pdf, linewidth=2, color='0.5')
plt.semilogx(_xlin, _ylin, 'k.')
#plt.semilogx(_xlin, pdftmp)

plt.show()
"""


# Starting over
df = pd.read_excel('Alluvial_river_bankfull_geometry__Phillips2022.xlsx')

nbins = 30

# Finite and gravel
taustar = df['tau_*bf'][ np.isfinite(df['tau_*bf']) * (df['D50 (m)'] > 0.002)]
log10taustar = np.log10(taustar)
bins = np.logspace( np.min(log10taustar), np.max(log10taustar), nbins+1)
bins = np.logspace( -3, 1, nbins+1)
hist = np.histogram(taustar, bins, density=True)

_y = hist[0]
_x = ( hist[1][1:] + hist[1][:-1] ) / 2.

#_shape, _loc, _scale = lognorm.fit(taustar)
_shape, _loc, _scale = lognorm.fit(taustar, floc=0)
_lognorm = lognorm(_shape, _loc, _scale)
_pdf = _lognorm.pdf(_x)

plt.figure()
# Probably best not to try and fit; just show the data
#plt.semilogx(_x, _pdf, linewidth=2, color='0.5')
#plt.semilogx(_x, _y, 'ko')
plt.hist(taustar, bins=bins, density=True, histtype='stepfilled', color='0.5',
                label='Bankfull Shields stress: $\\tau^*_\mathrm{bf}$')#:\n'+
                      #'Gravel-bed rivers from\n'+
                      #'Phillips et al. (2022)')
ax = plt.gca()
ax.set_xscale('log')
plt.ylabel('Probability density', fontsize=14)
plt.xlabel(r'Shields stress: $\tau^*$', fontsize=14)
plt.axvspan(0.03, 0.06, alpha=0.3, color='k', hatch='///',
                label=r'$0.03 \leq \tau^* \leq 0.06$')
plt.axvline(taustar.median(), color='k', linewidth=2,
                label=r'Median $\tau^*_\mathrm{bf}$ ='+'%.3f'%taustar.median())
plt.legend(fontsize=10)
plt.tight_layout()

"""
# Try gamma instead
_shape = gamma.fit(taustar) # 3 PARAMS IN "shape".
_gamma = gamma(*_shape)
_pdf = _gamma.pdf(_x)
plt.semilogx(_x, _pdf, linewidth=2, color='0.5')
plt.semilogx(_x, _y, 'k.')
"""


