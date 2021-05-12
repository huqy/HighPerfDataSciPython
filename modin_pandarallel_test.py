import time
import numpy as np

import pandas as pd

from pandarallel import pandarallel
pandarallel.initialize()

import modin.pandas as mpd

def func(x):
    return x**3

data=np.random.rand(100000,1000)
df=pd.DataFrame(data)

start=time.time()
df.apply(func, axis=1)
end=time.time()
print('Customized func: original pandas using ' + str(end-start)+' seconds')

start=time.time()
df.parallel_apply(func, axis=1)
end=time.time()
print('Customized func: pandarallel using ' + str(end-start)+' seconds')

start=time.time()
df.apply(max, axis=1)
end=time.time()
print('Internal max: original pandas using ' + str(end-start)+' seconds')

start=time.time()
df.parallel_apply(max, axis=1)
end=time.time()
print('Internal max: pandarallel using ' + str(end-start)+' seconds')

df=mpd.DataFrame(data)

start=time.time()
df.apply(func, axis=1)
end=time.time()
print('Customized func: modin using ' + str(end-start)+' seconds')

start=time.time()
df.apply(max, axis=1)
end=time.time()
print('Internal max: modin using ' + str(end-start)+' seconds')
