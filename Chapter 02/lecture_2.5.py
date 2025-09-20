'''Topic: String Methods'''

# |--------------|--------------------|--------------------------|-----------------------|
# |    Method    |    Description     |           Code           |        output         |
# |--------------|--------------------|--------------------------|-----------------------| 
# | Lower()      | Convert a string   | print(x.lower())         | python string method  |
# |              | into lower case.   |                          |                       | 
# |--------------|--------------------|--------------------------|-----------------------|
# | Upper()      | Convert a string   | print(x.upper())         | PYTHON STRING METHOD  | 
# |              | into upper case.   |                          |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | capitalize() | Convert the first  | print(x.capitaize())     | Python string method  |
# |              | character to upper |                          |                       |
# |              | case.              |                          |                       |
# |--------------|--------------------|--------------------------|-----------------------| 
# | title()      | Convert the first  | print(x.title())         | Pyhton String Method  |
# |              | character of each  |                          |                       |
# |              | word to upper case.|                          |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | swapcase()   | Swaps cases, lower | print(x.swapcase())      | PYThOn stRiNG MeTHoDs |
# |              | case becomes upper |                          |                       |
# |              | case & vice Versa. |                          |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | islower()    | return True if all | x = "python"             | True                  |
# |              | characters in the  | print(x.islower())       |                       |
# |              | string are lower   |--------------------------|-----------------------|
# |              | case.              | x = "Python"             | False                 |
# |              |                    | print(x.islower())       |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | isupper()    | return True if all | x = "PYTHON"             | True                  |
# |              | characters in the  | print(x.isupper())       |                       |
# |              | string are upper   |--------------------------|-----------------------|
# |              | case.              | x = "PYTHoN"             | False                 |
# |              |                    | print(x.islower())       |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | istitle()    | return True if the | x = "Python Good"        | True                  |
# |              | string follows the | print(x.istitle())       |                       |
# |              | rules of the title.|--------------------------|-----------------------|
# |              |                    | x = "Python good"        | False                 |
# |              |                    | print(x.istitle())       |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | isdigit()    | Returns True if all| x = '123'                | True                  |
# |              | characters in the  | print(x.isdigit())       |                       |
# |              | string are digits. |--------------------------|-----------------------|
# |              |                    | x = '123abc'             | False                 |
# |              |                    | print(x.isdigit())       |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | isalpha()    | Returns True if all| x = 'abc'                | True                  |
# |              | characters in the  | print(x.isalpha())       |                       |
# |              | string are in alp- |--------------------------|-----------------------|
# |              | -habets.           | x = 'abc123'             | False                 |
# |              |                    | print(x.isalpha())       |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | isalnum()    | Returns True if all| x = 'abc123'             | True                  |
# |              | characters in the  | print(x.isalnum())       |                       |
# |              | string are in alp- |--------------------------|-----------------------|
# |              | -habets-numeric    | x = 'abc123@#!'          | False                 |
# |              |                    | print(x.isalpha())       |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | strip()      | Returns a trimmed  | print(x.strip('-'))      | Python                |
# |              | version of the     |                          |                       |
# |              | string.            |                          |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | lstrip()     | Returns a left trim| print(x.lstrip('-'))     | Python-----           |
# |              | version of the     |                          |                       |
# |              | string.            |                          |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | rstrip()     | Returns a right    | print(x.rstrip('-'))     | -----Python           |
# |              | trim version of the|                          |                       |
# |              | string.            |                          |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | startswith() | Returns True if the| print(x.startswith('P')) | True                  |
# |              | string start with  |--------------------------|-----------------------|
# |              | the specified value| print(x.startswith('p')) | False                 |
# |--------------|--------------------|--------------------------|-----------------------|
# | endswith()   | Returns True if the| print(x.endswith('n'))   | True                  |
# |              | string ends with   |--------------------------|-----------------------|
# |              | the specified value| print(x.endswith(‘N'))   | False                 |
# |--------------|--------------------|--------------------------|-----------------------|
# | count()      | Returns the number | print(x.count('t'))      | 3                     |
# |              | of times aspecified|--------------------------|-----------------------|    
# |              | value occurs in a  | print(x.count(‘s'))      | 1                     |
# |              | string.            |                          |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | index()      | Searches the string| print(x.index('t'))      | 2                     |
# |              | for a specified    |                          |                       |
# |              | value and returns  |--------------------------|-----------------------|
# |              | the position of    | print(x.index(‘s'))      | 20                    |
# |              | where it was found.|                          |                       |
# |--------------|--------------------|--------------------------|-----------------------|
# | replace()    | Returns a string   | x = x.replace('S', 's')  | Python string methods |
# |              | where a specified  | x = x.replace('M', 'm')  |                       |
# |              | value is replaced  | print(x)                 |                       |
# |              | with a specified   |                          |                       |
# |              | value.             |                          |                       |
# |--------------|--------------------|--------------------------|-----------------------|

#method 1
str = "Welcome in Python"
print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title())

print(str.swapcase())
