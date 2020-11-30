#!/usr/bin/env python
# coding: utf-8

# # DAY 6

# In[8]:


test_list1=[1, 3, 4, 5, 6, 8]
res_list=[]
for i in range(0, len(test_list1)):
    res_list.append(test_list1[i] + 2)
print("Resultant list is : " + str(res_list))


# In[9]:


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()


# In[1]:


nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1


# In[2]:


#A number is said to be an armstrong number if it is equal to the sum of its own digit raised to the power of the number of digits. 

num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


# In[4]:


n=int(input())
if n<0:
    print("n is a negative number")
elif n>0:
    print("n is a positive number")
else:
    print("n is equal to zero")


# In[1]:


days= 5555  
years= days / 365  
print("Number of years is: ")
print(years)


# In[5]:


import math

print(math.sin(math.pi/3)) 
print(math.tan(math.pi/3))
print(math.cos(math.pi/6))


# In[6]:


print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")

