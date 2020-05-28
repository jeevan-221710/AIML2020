#!/usr/bin/env python
# coding: utf-8

# In[9]:


#program to print multiplication table
n=int(input("enter number"))
for i in range(1, 11):
   print(n, 'x', i, '=', n*i)


# In[11]:


#program to print the pattern
for i in range(6): # 0 1 2 3 4 5
    
    for j in range(i):
        print("*",end=" ")
    print("\n")


# In[12]:


#program to print fibonocii series of n number
n = int(input("enter n value "))
n1=0
n2 = 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count += 1


# In[13]:


#program to find roots of a qudratic equation
import cmath
a = int(input("enter a value"))
b = int(input("enter b value"))
c = int(input("enter c value"))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print(sol1)
print(sol2)


# In[14]:


#program to convert decimal number to binary number
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')
decimal = int(input("enter decimal no"))
convertToBinary(decimal)
print()


# In[ ]:




