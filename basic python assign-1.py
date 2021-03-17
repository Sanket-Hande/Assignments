#!/usr/bin/env python
# coding: utf-8

# # # Basic Python Assignment-1 

# Q1: In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
# * , 'hello', -87.8, - , /, + , 6
# 
# Ans: * = It is a multiple operator used in an expression. 
#      'hello' = It is a string (enclosed in single/double qoutes).
#      -87.4 = It is a floating point number. 
#      - = It is Subtraction operators mostly used in expressions.
#      / = It is a Division operators mostly used in expressions.
#      + = It is a Addition operators mostly used in expressions.
#      6 = It is an integer 
#      

# Q2: What is the difference between string and variable?
# 
# Ans: A string is a datatype for sequence of characters. It could contain anything from letter, spaces, to anything. To make strings we just need to enclose them in double or single quotes (" "/' ').
# Here "Spam" is a stirng. 
# Vairable are containers for storing data. 
# Here Spam is a variable.

# Q3: Describe three different data types.
# 
# Ans: The 3 basic datatypes in python are- 
#      1) int:- Integer datatypes are numbers without decimal point, example: 7, 5, 6, 46, 15 etc.
#      2) float:- Float datatypes are numbers with decimal point, example: 1.126512561, 4.99, etc.
#      3) string:- String is a datatype for sequence of characterss. example: "Sam", 'Jupyter', etc. 

# Q4: What is an expression made up of? What do all expressions do?
# 
# Ans Expression are combination of values,operators,variables. In simple language they are mathematical operations. Expressions are used in loops, with variables etc.
# example. y = 4*5/2, x-y+5, etc.
#  

# Q5: This assignment statements, like spam = 10. What is the difference between an
# expression and a statement?
# 
# Ans: Expressions are combination of values,operators,variables while statements are standalone
# statements which are performed in single go.
# 

# In[2]:


'''
Q6: After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1

Ans: output 23
'''
bacon =22
bacon +1


# In[8]:


'''
Q7: What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3

Ans: 'spam' + 'spamspam' = 'spamspamspam'
     'spam' *3 = 'spamspamspam'
'''

print('spam' + 'spamspam')
print('spam'* 3)


# Q8: Why is eggs a valid variable name while 100 is invalid?
# 
# Ans: 100 is a numeric value and int datatype whereas eggs doesnt correspond to any datatype or builtin function hence it is a valid variable. 

# Q9: What three functions can be used to get the integer, floating-point number, or string
# version of a value?
# 
# Ans To get integer value we use int(), for floatingpoint number we use float() and for string we use str(). 

# In[10]:


'''
Q10: Why does this expression cause an error? How can you fix it?
'I have eaten' + 99 +  'burritos'

Ans: We cannot concatinate string and integer datatype. We have to typecast 99 to string which could be achieved as- 
'I have eaten' +str(99) + 'burritos' or simply by add ' ' quotes to 99.
'''
'I have eaten ' + str(99) +  ' burritos'


# End of Assignment. 
