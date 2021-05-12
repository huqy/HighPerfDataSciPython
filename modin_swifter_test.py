import time
import numpy as np

import pandas as pd
import dask.dataframe as dd

def func(x):
    return x**3

data=np.random.rand(100000,1000)
df=pd.DataFrame(data)

import modin.pandas as mpd
import swifter

df=mpd.DataFrame(data)

start=time.time()
df.swifter.apply(func, axis=1)
end=time.time()
print('Customized func: modin swifter using ' + str(end-start)+' seconds')

start=time.time()
df.swifter.apply(max, axis=1)
end=time.time()
print('Internal max: modin swifter using ' + str(end-start)+' seconds')
