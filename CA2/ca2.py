import random
import sympy

# n , k = input().split(' ')
# n , k = int(n) , int(k)

numbers_of_attemp = []

##### Q1 #####
def monte_carlo(k , n) :
    counter = 0
    attemp = 0
    my_list = []
    for i in range(k) :
        my_list = [False]*n
        while counter != n:
            random_index = random.randint(0, len(my_list) - 1)
            random_element = my_list[random_index]
            if random_element == False :
                my_list[random_index] = True
                counter += 1

            attemp += 1
        numbers_of_attemp.append(attemp)
        counter = 0
        attemp = 0
        
        
##### Q2 #####        
n , k = 10 , 10
monte_carlo(k , n)
sum_number_of_attemp = 0
for i in numbers_of_attemp :
    sum_number_of_attemp += i

mean_attemp = sum_number_of_attemp / k
print('Avg number of attemps k = 10 , n = 10 :' , mean_attemp)
numbers_of_attemp.clear()

n , k = 10 , 100
monte_carlo(k , n)
sum_number_of_attemp = 0
for i in numbers_of_attemp :
    sum_number_of_attemp += i

mean_attemp = sum_number_of_attemp / k
print('Avg number of attemps k = 100 , n = 10:' , mean_attemp)
numbers_of_attemp.clear()

n , k = 10 , 1000
monte_carlo(k , n)
sum_number_of_attemp = 0
for i in numbers_of_attemp :
    sum_number_of_attemp += i

mean_attemp = sum_number_of_attemp / k
print('Avg number of attemps k = 1000 , n = 10 :' , mean_attemp)


##### Q3 Q4 Q5 #####
s = sympy.symbols('s')
i = sympy.symbols('i')
m = sympy.symbols('m')

probability = ((m - (i-1)) / m)

def calc(p) :
    return (p * sympy.E ** s)/(1-(1-p) * sympy.E ** s)

mgf_Xi = calc(probability)
print(mgf_Xi)


mgf_X = sympy.Product(mgf_Xi, (i , 1 , m))

list_of_mgf_x = []
for k in range(1 , n + 1) :
    p = probability.subs({i:k})
    list_of_mgf_x.append(calc(p))

for i in list_of_mgf_x :
    print(i)
    
print(mgf_X)
    
temp = sympy.diff(mgf_X , s)
expectation_x = temp.subs({m : 10 , s : 0}).evalf()
print(expectation_x)
