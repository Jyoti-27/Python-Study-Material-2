#!/usr/bin/env python
# coding: utf-8

# ### File Handling
# 
# - File handling is an important part of any web application.
# 
# - Python has several functions for creating, reading, updating, and deleting file

# #### File Handling
# - The key function for working with files in Python is the open() function.
# 
# - The open() function takes two parameters; filename, and mode.
# 

# There are four different methods (modes) for opening a file:
# 
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# 
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# 
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# 
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# 
# "t" - Text - Default value. Text mode
# 
# "b" - Binary - Binary mode (e.g. images)

# Syntax
# To open a file for reading it is enough to specify the name of the file:
# 
# - To open the file, use the built-in open() function.
# 
# - The open() function returns a file object, which has a read() method for reading the content of the file:

# In[6]:


file_txt = open("sample.txt","r")
print(file_txt.read())


# In[4]:


file_txt = open("C:/Users/Dell/Desktop/Data Folkz/IIIT Python/Revamp Python/sample.txt","r")
print(file_txt.read())


# - Read Only Parts of the File
# - By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# 

# In[7]:


#Example
#Return the 5 first characters of the file:
file_txt = open("sample.txt", "r")
print(file_txt.read(5))


# #### Read Lines
# - You can return one line by using the readline() method:
# 
# Example
# - Read one line of the file:
# 

# In[11]:


file_txt = open("sample.txt", "r")
print(file_txt.readline())
print(file_txt.readline())


# - By calling readline() two times, you can read the two first lines:

# In[9]:


file_txt = open("sample.txt", "r")
print(file_txt.readline())
print(file_txt.readline())


# By looping through the lines of the file, you can read the whole file, line by line:

# In[13]:


file_txt = open("sample.txt", "r")
for x in file_txt:
    print(x)


# #### Close Files
# It is a good practice to always close the file when you are done with it.

# In[15]:


file_txt = open("sample.txt", "r")
print(file_txt.readline())
file_txt.close()


# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

# #### Write to an Existing File
# - To write to an existing file, you must add a parameter to the open() function:
# 
# "a" - Append - will append to the end of the file
# 
# "w" - Write - will overwrite any existing content

# Example
# 
# Open the file "sample2.txt" and append content to the file:

# In[20]:


file_txt2 = open("sample2.txt", "a")
file_txt2.write("ola!Now there is new content")
file_txt2.close()

#open and read the file after the appending:
file_txt2 = open("sample2.txt", "r")
print(file_txt2.read())


# Example
# 
# Open the file "sample3.txt" and overwrite the content:

# In[25]:


file_txt3 = open("sample3.txt", "w")
file_txt3.write("Woops! I have deleted the content!")
file_txt3.close()

#open and read the file after the appending:
file_txt3 = open("sample3.txt", "r")
print(file_txt3.read())

