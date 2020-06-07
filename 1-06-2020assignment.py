#password picker
import string
from random import *
print("Welcome password Picker!!!!")
adj = ["Excellet","Very Good","Good","Bad","Poor"]
noun = ["jeevan","sai","narra","anaconda","jupyter"]
digits = string.digits
spl_char = string.punctuation
Welcome password Picker!!!!
while True:
    password = choice(adj) + choice(noun) + choice(digits) + choice(spl_char)
    print("Your Password is : ",password)
    print("Do you want to generate New password? ")
    response = input("Enter yes for New password and No for Not generating the password: ")
    if response in ["NO","no","No","nO"]:
        break
    elif response in ["Yes","yes"]:
        continue
    else:
        print("Enter Either Yes or No")
Your Password is :  Excelletjeevan5^
Do you want to generate New password? 
Enter yes for New password and No for Not generating the password: yes
Your Password is :  Poorsai4!
Do you want to generate New password? 
Enter yes for New password and No for Not generating the password: no
 
