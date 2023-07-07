'''
strings -> "" ''
str()

iterable
immutable
indexed
'''

st = "we are learning python"
#print(st)
#print(type(st))
#print(len(st))

# Indexing -> to get individual charavter value

#print(st[0])
#print(st[-1])
# its shows error
#st[0] = "W"
#print(st)
# TODO: slicing -> TO get a certain substring
#print(st[3 : 14])

#print(st.capitalize())
#print(st.title())
#print(st.upper())
#print(st.lower())

#print(st.count(" "))


# NOTE: If element is not present it gives ValueError
#print(st.index('e', 15, 17 ))
# NOTE: If element is not present it returns -1
#print(st.find('e' , 15, 17))

#print(st.startswith("we"))
#print(st.endswith("so"))
'''
# TODO: validating the strings
password = "abc123 "

password1 = "abc123"
# NOTE: It returns True only if string consist of alphabets and numbers
print(password.isalnum())
print(password1.isalnum())
password = "abd"
print(password.isalpha())

contact = "121313"
print(contact.isdigit())

password = "   "
password1 = ""
print(password.isspace())
print(password1.isspace())
'''
# TODO: split-> It splits the string into elements of a list on the basis of character provided
#st = "we are learning python"
#print(st.split(' ', 2))

#email = "John.Doe@google.com"
#domain = email.split("@")[1]
#print("Domain is: ",domain)

# TODO: replace
#st = "we are learning python"
#print(st.replace('a' , '@', 1))

# TODO: strip -> to remove extra spaces
# password = "     njhsbhvff     "
# print("left strip: ",password.lstrip())
# print("right strip: ",password.rstrip())
# print("strip: ",password.strip())

# TODO: join -> joining different strings with a given substring
# fname = "john"
# lname = "doe"
# uname = ".".join([fname , lname])
# print(uname)

# domain = "abc.com"
# email = "@".join([uname, domain])
# print(email)


# TODO: format()
n1 = 3
n2 = 5
ans = n1 + n2

# print(str(n1) + "+" + str(n2) + "=" + str(ans))

# print("{1} + {0} = {2}".format(n1, n2, ans))

#print("2" + "2")

# TODO: escape sequences
'''
# \b -> backspace
# \t -> tab
# \n -> new line
# \a -> alert
# \\ -> \
# \' -> '
# '''
#path = r'C:\temp\navin\new_folder'
#print(path)

s='python'
print(s.find('y'))
# 1
print(s.find('a'))
# -1
