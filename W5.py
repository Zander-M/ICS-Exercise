from matplotlib import pyplot
from math import log
from math import exp
a = pyplot
x = [i * 0.1 for i in range(10)]
cy = [j for j in x]
logy = [log(k, 2) for k in x]
quadray = [int(l**2) for l in x]
cuby = [int(m**2) for m in x]
nlogy = [int(n * log(n)) for n in x]
expoy = [int(exp(2**m)) for m in x]
a.plot(x, cy, label='linear')
a.plot(x, logy, label='log')
a.plot(x, quadray, label="quadratic")
a.plot(x, cuby, label="cubic")
a.plot(x, nlogy, label="n*log(n")
a.legend()
a.show(100, 500
       )


import time


def timeit (f, *args):
	a = time.time()
	f(*args)
	b = time.time()
	return b - a