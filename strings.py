str1="my name is sandeep"
print(str1)
#to find the occurence of a particular character, counts the occurence
#length of the string
print(str1.find('s'))
print(str1.count('s'))
print(len(str1))
#is a decimal value or not
print(str1.isdecimal())
#is a number or not
print(str1.isalnum())
#is an alphabet or not
print(str1.isalpha())
#i=has a n ascii value or not
print(str1.isascii())
#is a digit or not
print(str1.isdigit())
#are all values lower case or not
print(str1.islower())
#string have characters without space
print(str1.isidentifier())
str2="python"
print(str2.isidentifier())
#converting upper and lower case
print(str1.upper())
print(str1.lower())
#capitalize the first lette
print(str1.capitalize())
#centering
print(str1.center(45,'*'))
#ignoring case sensitivity
print(str1.casefold())
#to check string ends with
print(str1.endswith('deep'))
#expanding the tab size
str23="hello"
print(str23.expandtabs(23))
#using title
print(str1.title())
#left justing and right justing
print(str23.ljust(24,'*'))
print(str23.rjust(24,'*'))
#case swapping
print(str1.swapcase())
#partitioning
print(str1.partition('is'))
#replace
print(str1.replace('a','A',2))