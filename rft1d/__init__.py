__version__ = "0.2.0"  # (2022.02.22)

from . import distributions, geom, prob, random

randn1d = random.randn1d
multirandn1d = random.multirandn1d

chi2 = distributions.chi2
f = distributions.f
norm = distributions.norm
t = distributions.t
T2 = distributions.T2
