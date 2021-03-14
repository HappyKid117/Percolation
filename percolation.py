import random

global n
global A
n = int(input())

p = float(input())
k = int((n*n*p))
A = [0]*((n**2)+2)
path = [0]*1
for i in range((n**2) + 2):
    A[i] = i

opensite = [0]*((n**2)+2)
opensite[0] = 1
opensite[-1] = 1

sz = [0]*((n**2)+2)

def printArr(A):
    #print(A[0])
    for i in range(n):
        for j in range(n):
            if A[(n*i)+j+1]==1:
                print(' ', end=" ")
            else:
                print(0, end=" ")
        print()
    #print(A[-1])

def root(p):
    while(A[p]!=p):
        A[p]=A[A[p]]
        p = A[p]
    return p


def union(p, q):
    proot = root(p)
    qroot = root(q)
    if qroot == proot:
        return
    if(sz[proot]<sz[qroot]):
        A[proot] = qroot
        sz[qroot] += sz[proot]
    else:
        A[qroot] = proot
        sz[proot] += sz[qroot]



def isConnect(p, q):
    if root(p) == root(q):
        return 1
    else:
        return 0

def openit(p):
    opensite[p] = 1

def conv(r1, c1):
    return (n*(r1-1)+c1)

def checkenv(r1, c1):
    p = conv(r1, c1)

    if(r1>1 and opensite[conv(r1-1, c1)]==1):
        if(isConnect(conv(r1-1, c1), p)==0):
            union(conv(r1-1, c1), p)
    if(r1<n and opensite[conv(r1+1, c1)]==1):
        if(isConnect(conv(r1+1, c1), p)==0):
            union(conv(r1+1, c1), p)
    if(c1>1 and opensite[conv(r1, c1-1)]==1):
        if(isConnect(conv(r1, c1-1), p)==0):
            union(conv(r1, c1-1), p)
    if(c1<n and opensite[conv(r1, c1+1)]==1):
        if(isConnect(conv(r1, c1+1), p)==0):
            union(conv(r1, c1+1), p)


def establish():
    for i in range(1, n+1):
        union(0, i)
        union((n**2)+1, (n**2)-i+1)

#printArr(opensite)
establish()
while(True):
    r1, c1 = random.randint(1, n), random.randint(1, n)
    
    if(opensite[conv(r1, c1)]==0):
        openit(conv(r1, c1))
        checkenv(r1, c1)
        if(isConnect((n**2)+1, 0)==1):
            print()
            break
        k=k-1
    
    if k==0:
        break

print("Grid size: ", n, "x", n)
print("Probability of open site: ", p*100, "%")
print()
printArr(opensite)
print()
if k==0:
    print("Not Percolated")
else:
    print("Percolated")
print("Number of open sites: ", opensite.count(1)-2)
print("Percentage of open sites: ", ((opensite.count(1)-2)/n**2)*100, "%")