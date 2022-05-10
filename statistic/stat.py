
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("data.csv")
df['temperature'].plot(kind='bar')

df_v = pd.DataFrame(data={'temp': df['temperature']})

df_v.plot.kde()
plt.show()
exp = df_v['temp']

print(stats.kstest(exp, 'norm', (exp.mean(), exp.std()), N=5000))

