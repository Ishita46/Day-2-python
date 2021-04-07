Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file = open('C:/Users/ishit/OneDrive/Desktop/ishita.txt')
>>> file.read()
'hi my name is ishita bansal \nI am 12+ years old.'
>>> file = open('C:/Users/ishit/OneDrive/Desktop/ishita.txt')
>>> file.readlines()
['hi my name is ishita bansal \n', 'I am 12+ years old.']
>>> name = "My name is Ishita Bansal"
>>> name.split()
['My', 'name', 'is', 'Ishita', 'Bansal']
>>> name = "My name is Ishita Bansal. I am 12+ years old. I study in GDGPS. My hobbies are to do swimming, play tennis and play basketball."
>>> name.split()
['My', 'name', 'is', 'Ishita', 'Bansal.', 'I', 'am', '12+', 'years', 'old.', 'I', 'study', 'in', 'GDGPS.', 'My', 'hobbies', 'are', 'to', 'do', 'swimming,', 'play', 'tennis', 'and', 'play', 'basketball.']
>>> name.split(",")
['My name is Ishita Bansal. I am 12+ years old. I study in GDGPS. My hobbies are to do swimming', ' play tennis and play basketball.']
>>> name.split(".")
['My name is Ishita Bansal', ' I am 12+ years old', ' I study in GDGPS', ' My hobbies are to do swimming, play tennis and play basketball', '']
>>> def greet(name):
	print("hello " +name+ " .I welcome you in my class");

	
>>> greet("Ishita")
hello Ishita .I welcome you in my class
>>> def words():
	filename = input("enter file name ")
	numberofwords = 0 
	file = open(filename, 'r')
	for i in file:
		words = line.split()
		numberofwords = numberofwords + len(words)
	print("number of words in the file are")
	print(numberofwords)

	
>>> words()
enter file name C:/Users/ishit/OneDrive/Desktop/ishita.txt
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    words()
  File "<pyshell#25>", line 6, in words
    words = line.split()
NameError: name 'line' is not defined
>>> def words():
	filename = input("enter file name ")
	numberofwords = 0 
	file = open(filename, 'r')
	for i in file:
		words = i.split()
		numberofwords = numberofwords + len(words)
	print("number of words in the file are")
	print(numberofwords)

	
>>> words()
enter file name C:/Users/ishit/OneDrive/Desktop/ishita.txt
number of words in the file are
11
>>> 