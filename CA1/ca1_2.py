import matplotlib.pyplot as plt
from scipy.stats import distributions as dist 

i = range(250)
rvb = dist.binom(250 , 0.008)
rvp = dist.poisson(2)
rvn = dist.norm(2 , 1.984)

plt.vlines(i , 0 , rvb.pmf(i) , colors='r' , linestyles= '-' , linewidth = 3 , label='prob')
plt.vlines(i , 0 , rvp.pmf(i) , colors='b' , linestyles= '-' , linewidth = 1 , label='prob')
plt.vlines(i , 0 , rvn.pdf(i) , colors='g' , linestyles= '-' , linewidth = 2 , label='prob')
plt.show()