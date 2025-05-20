import matplotlib.pyplot as plt
from scipy.stats import distributions as dist 

i = range(7072)
rvb = dist.binom(7072 , 0.45)
rvp = dist.poisson(3182.59)
rvn = dist.norm(3182.59 , 41.84)

plt.vlines(i , 0 , rvb.pmf(i) , colors='r' , linestyles= '-' , linewidth = 2 , label='prob')
plt.vlines(i , 0 , rvp.pmf(i) , colors='b' , linestyles= '-' , linewidth = 3 , label='prob')
plt.vlines(i , 0 , rvn.pdf(i) , colors='g' , linestyles= '-' , linewidth = 0.5 , label='prob')
plt.show()