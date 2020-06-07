#Read the input as two limits and Print the output as Palindrome count between the two limits

maximum = int(input(" Please Enter the Maximum Value : "))
minimum = int(input(" Please Enter the Minimum Value : "))
count=0
for num in range(1, maximum + 1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10
        
    if(num == reverse):
        count=count+1
print( count, end = '  ')
 Please Enter the Maximum Value : 10
 Please Enter the Minimum Value : 1
 
 9  

#Test case1:
    #    string →  "((((()()()))))()"
     #  output →  8
   # Test case2:
    #    string →  "((()))()"
    #    Output →  4

str=input("enter string")
cnt=0
c=0
c0=0
for i in str:
    if i=='(':
        cnt=cnt+1;
    elif i==')':
        c=c+1
if (cnt==c):
    print(cnt)
else:
    print("error")


#Accept input as a string and display sum of digits as the output 

str=input("enter string")
sum_digit = 0
for x in str:
    if x.isdigit() == True:
        z = int(x)
        sum_digit = sum_digit + z
print(sum_digit)
enter stringAppli123cation456 
21


#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85

n=float(input("enter score"))

if(n==0.9):
    print("A")
elif(n==0.8):
    print("B")
elif(n==0.7):
    print("C")
elif(n==0.6):
    print("D")
elif(n<0.6):
    print("F")
else:
    print("out of range")
enter score0.2
F


#Write a Python program to find the median of three values.

a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median is", median)
Input first number: 26
Input second number: 15
Input third number: 29
The median is 26


#Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" 
#instead of the number and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".

for fizzbuzz in range(1,51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz
31
32
fizz
34
buzz
fizz
37
38
fizz
buzz
41
fizz
43
44
fizzbuzz
46
47
fizz
49
buzz


#Accept a number as an input and check whether the given number is palindrome or not
#if it is a palindrome number print the number on the screen
#if it is not a palindrome number reverse that number and add it to previous number
#repeat this until will get a palindrome number and print that palindrome number on the screen

n = int(input())
while True :
    if str(n) == str(n)[::-1]:
        print(str(n)[::-1],"is a palindrome")
        break
    else:
        n += int(str(n)[::-1])
127
848 is a palindrome
 
#Accept a string from the user and count no.of vowels,consonants and special characters

def countCharacterType(str):
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0 
    for i in range(0, len(str)):  
        ch = str[i]  
        if ( (ch >= 'a' and ch <= 'z') or 
             (ch >= 'A' and ch <= 'Z') ):
            
            ch = ch.lower() 
  
            if (ch == 'a' or ch == 'e' or ch == 'i' 
                        or ch == 'o' or ch == 'u'): 
                vowels += 1
            else: 
                consonant += 1
          
        elif (ch >= '0' and ch <= '9'): 
            digit += 1
        else: 
            specialChar += 1
      
    print("Vowels:", vowels) 
    print("Consonant:", consonant)  
    print("Digit:", digit)  
    print("Special Character:", specialChar)  
str = "Jeevan narra 123!@#$"
countCharacterType(str)  
Vowels: 5
Consonant: 6
Digit: 3
Special Character: 6
 
