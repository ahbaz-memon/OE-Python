#!/usr/bin/env python
# coding: utf-8

# # A.Python Program to implement following concept

# ### 1.Operators

# ##### a.arithmatic Operators

# In[1]:


a = 10 
b = 3


# In[2]:


print('addition : ', a + b)
print('subtraction : ', a - b)
print('multiplication : ', a * b)
print('division : ', a / b)
print('floor division: ', a // b)
print('modulus : ', a % b)


# ##### b.logical operators

# In[3]:


a = True
b = False


# In[4]:


print('and : ', a and b)
print('or : ', a or b)
print('not : ', not a)


# ##### c.bitwise operators

# In[5]:


n = 25


# In[6]:


print('right shift', 25 >> 2)
print('left shift', 25 << 2)


# ##### d.assignment operators

# In[7]:


n = 25


# In[8]:


print('is equal', n == 20)

n += 2
print('add', n)

n -= 2
print('sub', n)

n *= 2
print('mul', n)

n /= 20
print('div', n)


# ##### e.relational operators

# In[9]:


a = 10
b = 3


# In[10]:


print('is equal', a == b)
print('is not equal', a != b)
print('is greater than', a > b)
print('is greater than and equal', a >= b)
print('is less than', a < b)
print('is less than and equal', a <= b)


# ### 2.Range Function

# In[11]:


list(range(5)) # the range for 0 to 4


# In[12]:


list(range(1, 21, 2)) # the range for 1 to 20 with incr 2


# In[13]:


list(range(1, -15, -3)) # the range for 1 to -15 with decr 3


# ### 3.For Loop

# In[14]:


# printing only multiple of 5
for e in range(1, 20 + 1):
    if e % 5 == 0:
        print(e, end = ' ')


# ### 4.While Loop

# In[16]:


# printing other than multiple of 5
i = 0
while i < 20:
    i += 1
    if i % 5 == 0:
        continue
    print(i, end = ' ')


# # B.Python Program to display all prime numbers within an interval 11 to 50

# In[17]:


def isprime(n):
    '''
    funtion for checking
    whether a number n is prime or not
    '''
    flag = True
    for e in range(2, n, 1):
        if n % e == 0:
            flag = False
            break
    return flag


# In[18]:


isprime(14) # is 14 a prime?


# In[19]:


isprime(17) # is 17 a prime?


# In[20]:


start = int(input("Enter starting point for displaying prime numbers : ")) # starting range
end = int(input("Enter ending point for displaying prime numbers : ")) # ending range

print()
print("The prime numbers are :")
for e in range(start, end + 1, 1):
    if isprime(e):
        print(e, end = ' ') # printing prime nubers


# # C.Python Program to check given number is even or odd

# In[21]:


def Even_or_Odd(n):
    '''
    function for checking
    a number is even or odd
    '''
    result = n % 2
    if result == 0:
        return 'even'
    else:
        return 'odd'


# In[22]:


n = int(input("Enter a number to know its even or odd : ")) # inputing a number

print()
print('Number ' + str(n) + ' is a ' + Even_or_Odd(n) + '.') # is even or oddd ?


# In[23]:


n = int(input("Enter a number to know its even or odd : ")) # inputing a number

print()
print('Number ' + str(n) + ' is a ' + Even_or_Odd(n) + '.') # is even or oddd ?


# In[ ]:




