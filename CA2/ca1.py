import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import poisson , binom

df = pd.read_csv('Tarbiat.csv')

###### Q1 ######
plt.hist(df['BRT'] , bins=range(min(df['BRT']) , max(df['BRT']) + 1) , color='red' , edgecolor ='red' , alpha=0.5 , label='BRT')
plt.hist(df['metro'], bins=range(min(df['metro']), max(df['metro']) + 1),color='blue' ,  edgecolor='blue' , alpha = 0.5 , label='Metro')
plt.title('Histogram of Data Metro and BRT')
plt.xlabel('Value')
plt.ylabel('Size')
plt.legend()


##### Q2 ######
# mean_value_metro = df['metro'].mean()
# mean_value_BRT = df['BRT'].mean()
# poisson_param_metro = mean_value_metro
# poission_param_BRT = mean_value_BRT
# print(f"Estimated Poisson parameter (lambda): {poisson_param_metro}")
# print(f"Estimated Poisson parameter (lambda): {poission_param_BRT}")


##### Q3 #####
# plt.hist(df['metro'] ,bins=range(min(df['metro']), max(df['metro']) + 1) ,  density=True, color='blue' , edgecolor='blue' , alpha = 0.5 , label='Metro')
# plt.title('Histogram of Data Metro and BRT')
# plt.xlabel('Value')
# plt.ylabel('Size')
# plt.legend()



##### Q4 #####
# data = np.random.poisson(poisson_param_metro, 9999)
# plt.hist(data, bins=np.arange(0, max(data) + 1), density=True , edgecolor='red', alpha=0.3, color='red' , label='Metro check')
# x_values = np.arange(0, max(data) + 1)
# plt.legend()



##### Q5 #####
# parameter_sum = poisson_param_metro + poission_param_BRT
# data = np.random.poisson(parameter_sum, 9999)
# plt.hist(data, bins=np.arange(0, max(data) + 1), density=True , edgecolor='blue', alpha=0.5, color='blue' , label='sum metro brt labmda')
# x_values = np.arange(0, max(data) + 1)
# sum = df['metro'] + df['BRT']
# plt.hist(sum , bins=range(0 , max(sum) + 1) , density=True , color='red' , edgecolor ='red' , alpha=0.5 , label='sum metro brt')
# x_values = np.arange(0, max(sum) + 1)
# plt.legend()



##### Q7 #####
# n = 8
# p = poisson_param_metro / parameter_sum
# x_values = np.arange(0, n+1)
# binom_pmf = binom.pmf(x_values, n, p)
# plt.bar(x_values, binom_pmf, align='center' , alpha=0.7, color='blue' , label='w ~ p(x|x+y=8)')
# plt.title('Binomial Distribution')
# plt.xlabel('Number of Successes')
# plt.ylabel('Probability Mass Function (PMF)')
# plt.legend()



##### Q8 #####
# sum_row = df.sum(axis=1)
# def is_equal_to_8(x):
#     return x == 8
# condition = is_equal_to_8(sum_row)
# df_sum_8 = df[condition]
# print(df_sum_8)
# pmf_values = df_sum_8['metro'].value_counts(normalize=True).sort_index()
# plt.bar(pmf_values.index, pmf_values, align='center', alpha=0.4, color='red', label='metro on condition that sum Metro & BRT equal 8')
# plt.title('Probability Mass Function (PMF) of DataFrame')
# plt.xlabel('Values')
# plt.ylabel('Probability')
# plt.legend()






plt.show()