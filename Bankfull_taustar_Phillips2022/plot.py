import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import lognorm, gamma

plt.ion()

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
# Not labeling because this is the x/y axis main plot
plt.hist(taustar, bins=bins, density=False, histtype='stepfilled', color='0.5')#,
                #label='Bankfull bed\nShields stress: $\\tau^*_{b,\mathrm{bf}}$')#:\n'+
                      #'Gravel-bed rivers from\n'+
                      #'Phillips et al. (2022)')

#plt.figure()
#plt.hist( np.log10(taustar), bins=np.linspace(-3,1,30), density=True, histtype='stepfilled', color='0.5')

ax = plt.gca()
ax.set_xscale('log')
plt.ylabel('Number of rivers', fontsize=14)
plt.xlabel(r'Bankfull bed Shields stress: $\tau^*_b$', fontsize=14)
plt.axvspan(0.036, 0.072, alpha=0.3, color='k', hatch='///',
                label=r'$0.036 \leq \tau^*_b \leq 0.072$')
plt.axvline(taustar.median(), color='k', linewidth=2,
                label=r'Median $\tau^*_\mathrm{bf}$ ='+'%.3f'%taustar.median())
plt.legend(fontsize=10)
plt.tight_layout()

plt.savefig('bankfull_taustar_Phillips2022.pdf')

