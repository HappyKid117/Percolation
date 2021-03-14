import random
n = 1000
p = 0.50
print(n)
k = int((n*n*p))
for i in range(k):
    print(random.randint(1, n), random.randint(1, n))
print(0, 0)