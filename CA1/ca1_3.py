import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import distributions as dist 

i = np.random.normal(80 , 12 , size = 400)
print(i)
rvn = dist.norm(80 , 12)

sadak90 = rvn.ppf(0.9)
print('min grade to above 90 percent of student :' , sadak90)

charak3 = rvn.ppf(0.75)
charak2 = rvn.ppf(0.25)
print('probability that x between charak 2 and charak 3 (' , charak2 , charak3 , ')')
F90 = rvn.cdf(90)
F80 = rvn.cdf(80)
print('probability that 80 < X < 90 : ' , F90 - F80)


plt.vlines(i , 0 , rvn.pdf(i) , colors='g' , linestyles= '-' , linewidth = 2)
plt.axvline(charak2 , linewidth = 1 , color = 'b')
plt.axvline(charak3 , linewidth = 1 , color = 'b')
plt.axvline(sadak90 , linewidth = 1 , color = 'r')
plt.show()