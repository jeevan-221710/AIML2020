#Q1)Create a function to find Factorial of a number using Recursion

def rfactorial(n):
    if(n==1):
        return 1
    else:
        return n*rfactorial(n-1)
    
rfactorial(8)           
40320
#Q2)Create a function and display ‘n’ Fibonacci numbers using Recursion

def nfib(n):
    if(n==1)or(n==0):
        return n
    else:
        return (nfib(n-1)+nfib(n-2))
k=int(input("enter value of n:"))
for i in range(k):
    print(nfib(i),end=",")

nfib(4)    
enter value of n:5
0,1,1,2,3,
3
#Q3)Print sum of list of elements without using sum() function

def k_list(elements):   
    s = 0 
    for i in elements:
        s += i
    print (s)

k_list([2,3,4,1])
10
#Q4)print only even numbers from the list

def p_list(kites):
    for z in kites:
        if(z%2==0):
            print(z,end=",")
p_list([1,2,3,4,6,7,8])            
2,4,6,8,
#Q5)Write a Python program to get the smallest number from a list and display index of smallest element of the list

def c_list(cars):
    for i in cars:
        p=min(cars)
        return(p)
    return(cars.index(p))

c_list([5,6,8,3,9])
3
#Q6)Write a Python function that checks whether a passed string is palindrome or not

def Palin_check(s): 
    return s == s[::-1] 
 
s = input("enter string:")
ans = Palin_check(s) 
  
if ans: 
    print("Yes it is palindrome") 
else: 
    print("No its not a palindrome") 
    
enter string:nitin
Yes it is palindrome
#Q7)Write a Python program to count the number of even and odd numbers from a series of numbers. 
#Sample numbers : numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Output :
#Number of even numbers : 4
#Number of odd numbers : 5

list1=[]
e=0
o=0
n=int(input("enter number of elements:"))
for i in range(0,n+1):
    z=int(input("enter value:"))#we are taking list elements with user
    list1.append(z)
print(list1) 
for p in list1:
    if(p%2==0):
        e+=1
    else:
        o+=1
print("Number of even numbers:",e)
print("Number of odd numbers:",o)
enter number of elements:5
enter value:2
enter value:3
enter value:6
enter value:5
enter value:4
enter value:8
[2, 3, 6, 5, 4, 8]
Number of even numbers: 4
Number of odd numbers: 2
#Q8)Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
#Expected Output : 0 1 2 4 5

for r in range(0,7):
    if r==3 or r==6:
        continue
    print(r,end=" ")    
0 1 2 4 5 
#Q9)Write a python function to check whether the given number is prime or not

def prime_check(n):
    c=0
    for i in range(1,n):
        if(n%i==0):
            c+=1
    if(c>1):
        print(n,"is not a prime number")
    else:
        print(n,"is a prime number")
    
prime_check(4)   
prime_check(5)
prime_check(9)
prime_check(29)
            
4 is not a prime number
5 is a prime number
9 is not a prime number
29 is a prime number
#Q10)Write a python function to check whether the given number is Adam number or not
#Example: 
#Input : 12
#Output : Adam Number

#Explanation: 12*12 = 144
#Reverse of 12 is 21 → 21*21 =441
#Reverse of 144 == 441

n =input()
reverse=n[::-1]
n_sqr=int(n)**2
reverse_sqr=int(reverse )**2
if int(n_sqr )==int(str(reverse_sqr)[::-1]):
   print("adam number")
else:
   print("not an adam number")
121
adam number
