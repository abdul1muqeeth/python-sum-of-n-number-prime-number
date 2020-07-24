#!/usr/bin/env python
# coding: utf-8

# In[1]:


number = int(input("Please Enter any Number: "))

total = 0
value = 1

while (value <= number):
    total = total + value
    value = value + 1

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))


# In[7]:


num =int(input("Enter the number"))
  
# If given number is greater than 1 
if num > 1:  
   for i in range(2, num): 
          
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
       else: 
        print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 
       


# In[ ]:




