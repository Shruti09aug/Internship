#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#11. Write a python program to find the factorial of a number.
import math
def factorial(n):
    return(math.factorial(n))
 
num = int(input("Enter number: "))
print("Factorial of", num, "is",factorial(num))


# In[ ]:


#12. Write a python program to find whether a number is prime or composite.
num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")


# In[ ]:


#13. Write a python program to check whether a given string is palindrome or not.

def reverse(str1):
    if(len(str1) == 0):
        return str1
    else:
        return reverse(str1[1 : ]) + str1[0]
    
string = input("Please enter your own : ")
str1 = reverse(string)
print("String in reverse Order :  ", str1)

if(string == str1):
   print("This is a Palindrome String")
else:
   print("This is Not")


# In[ ]:


#14.Write a Python program to get the third side of right-angled triangle from two given sides.
def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"


# In[ ]:


#15.Write a python program to print the frequency of each of the character present in a given string. 
str1 = input ("Enter the string: ")
d = dict()
for c in str1:
    d[c] = d.get(c, 0) + 1
print(d)


# In[ ]:




