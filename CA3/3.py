import numpy as np, random
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


def set_seed(seed):
    np.random.seed(seed)
    random.seed(seed)
    
set_seed(810109203)

df = pd.read_csv('FIFA2020.csv', encoding = "ISO-8859-1")

print(df)

mean_pace = df['pace'].mean()
df['pace'] = df['pace'].fillna(mean_pace)
mean_dribbling = df['dribbling'].mean()
df['dribbling'] = df['dribbling'].fillna(mean_dribbling)

print(df)
df.to_csv('my edit')

bin_tuple = tuple(i for i in range(0 , 100))
# # plt.boxplot(df['age'])
# # plt.yticks(bin_tuple)
# max_age = df['age'].max()
# min_age = df['age'].min()
# print('max age:' , max_age , 'min age:' , min_age)
# q1_age = df['age'].quantile(0.25)
# q2_age = df['age'].quantile(0.5)
# q3_age = df['age'].quantile(0.75)
# print('Q1 age:' , q1_age , 'Q2 age:' , q2_age , 'Q3 age:' , q3_age)

temp_data = df['weight'].sample(n = 100, replace=False)
print("mean:",np.mean(temp_data))
print("var:",np.var(temp_data))
print("std:",np.std(temp_data))

temp_sample = np.random.normal(np.mean(temp_data), np.std(temp_data), 100)
quantiles_norm = np.percentile(temp_sample, bin_tuple)
quantiles_data = np.percentile(temp_data, bin_tuple)
# plt.plot(quantiles_norm, quantiles_data)
# plt.plot([min(quantiles_norm), max(quantiles_norm)] , [min(quantiles_data), max(quantiles_data)] , color='red')


statistic, p_value = stats.shapiro(temp_data)
print("p_value:", p_value)
print("statistic:" , statistic)

# temp_data = df['weight'].sample(n = 500, replace=False)
# print("mean:",np.mean(temp_data))
# print("var:",np.var(temp_data))
# print("std:",np.std(temp_data))

# temp_sample = np.random.normal(np.mean(temp_data), np.std(temp_data), 500)
# quantiles_norm = np.percentile(temp_sample, bin_tuple)
# quantiles_data = np.percentile(temp_data, bin_tuple)
# plt.plot(quantiles_norm, quantiles_data)
# plt.plot([min(quantiles_norm), max(quantiles_norm)] , [min(quantiles_data), max(quantiles_data)] , color='red')


# statistic, p_value = stats.shapiro(temp_data)
# print("p_value:", p_value)
# print("statistic:" , statistic)

# temp_data = df['weight'].sample(n = 2000, replace=False)
# print("mean:",np.mean(temp_data))
# print("var:",np.var(temp_data))
# print("std:",np.std(temp_data))

# temp_sample = np.random.normal(np.mean(temp_data), np.std(temp_data), 2000)
# quantiles_norm = np.percentile(temp_sample, bin_tuple)
# quantiles_data = np.percentile(temp_data, bin_tuple)
# plt.plot(quantiles_norm, quantiles_data)
# plt.plot([min(quantiles_norm), max(quantiles_norm)] , [min(quantiles_data), max(quantiles_data)] , color='red')


# statistic, p_value = stats.shapiro(temp_data)
# print("p_value:", p_value)
# print("statistic:" , statistic)

# bin2_tupple = tuple(i for i in range(0 , 20))
# poisson_data = np.random.poisson(3, 5000)
# poisson_data_hist = plt.hist(poisson_data, bins=bin2_tupple)

# random_data = np.random.poisson(3 * 5, 5)
# statistic, p_value = stats.shapiro(random_data)
# stats.probplot(random_data, dist="norm", plot=plt)
# print("p_value:" , p_value)

# random_data = np.random.poisson(3 * 50, 50)
# statistic, p_value = stats.shapiro(random_data)
# stats.probplot(random_data, dist="norm", plot=plt)
# print("p_value:" , p_value)

random_data = np.random.poisson(3 * 5000, 5000)
statistic, p_value = stats.shapiro(random_data)
stats.probplot(random_data, dist="norm", plot=plt)
print("p_value:" , p_value)


plt.show()