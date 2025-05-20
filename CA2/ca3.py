import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from time import sleep
from IPython import display

df = pd.read_csv('digits.csv')

index_row = 200
row_201_data_list = df.iloc[index_row].tolist()

index_row = 201
row_202_data_list = df.iloc[index_row].tolist()

df = df.drop(index=200)
df = df.drop(index=201)

threshold_value = 128
columns_to_threshold = df.columns.difference(['label'])
df[columns_to_threshold] = df[columns_to_threshold].map(lambda x: 1 if x >= threshold_value else 0)

select_row = df.iloc[119].tolist()
select_row = select_row[1:]
reshaped_array = np.array(select_row).reshape((28, 28))
print(reshaped_array)

# plt.imshow(reshaped_array)

t = 1000
p = np.linspace(0,1,t)
fy = stats.beta.pdf(p, a=1, b=1)

def update(fy: np.array, n:bool) -> np.array:
    p = np.linspace(0,1,t)
    # calculate P(N = n| Y = p) which is a bernouli distribution
    # calculate integral(0 -> 1) fy * pny
    pny = stats.bernoulli.pmf(n , p)
    integral = np.sum(fy * pny) / t
    post = fy * pny / integral
    return post

plt.figure(figsize=(10,8))
for i in range(100):
    # replace 'df' with your dataframe's name, this is just a suggestion, you do not have to code exactly like this
    n =  df[df['label'] == 8].iloc[i, df.columns.get_loc('pixel404')]
    fy = update(fy, n)

    # dynamic plot
    # do not change this part
    plt.plot(p, fy, 'r', label='1')
    plt.ylim(-1, 10)
    plt.xlim(0, 1)
    plt.text(0.1,9,f'number of seen data : {i + 1}, p = {fy.argmax() / t :.2f}', color='purple')
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    sleep(0.05)
    
# plt.show()
df.to_csv('sobhan.csv')