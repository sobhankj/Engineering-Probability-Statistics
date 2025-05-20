# import choice 
import numpy as np 
import matplotlib.pyplot as plt 

n = 500
m = 5000
pr = float(input('enter p to plot it (0 to 1) : '))
probi = [1-pr , pr]

def gereftan_tozi(n , m , prob) :
    #create matrice m * n with costomize probebility (prob)
    random_choice_bernoulli = np.random.choice(2, n*m , p = prob)
    random_choice_bernoulli = np.reshape(random_choice_bernoulli, (m, n))
    
    #sumation each i in m
    sum_satr_array = np.sum(random_choice_bernoulli , axis= 1)
    
    # expectation each i in m
    expectation = np.divide(sum_satr_array , n)
    
    # expectation all 500 element with 5000 tozie with function np.mean
    exx = np.mean(sum_satr_array)
    
    # variance all 500 element with 5000 tozie with function np.var
    variance = np.var(sum_satr_array)
    
    return random_choice_bernoulli , sum_satr_array , exx , variance , expectation
    
rand , sumi , ex , var , expec_array = gereftan_tozi(n , m , probi)

e = n * probi[1]
v = n * probi[1] * probi[0]

print('sum of all satr in test ->' , sumi)
print('expectation of each test ->' , expec_array)
print('expectation of all test ->' , ex)
print('formula expectation =' , e)
print('variance of all test ->' , var)
print('formula variance =' , v)

plt.hist(rand , edgecolor = 'black' , histtype= 'bar')
plt.show()