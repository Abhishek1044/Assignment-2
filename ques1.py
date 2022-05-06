given_str="Python is a case sensitive language"

# a part
print(len(given_str))

# b part
print(given_str[: : -1])

# c part
newstr = given_str[10:26]
print(newstr)

# d part
given_str=given_str.replace(newstr,"object oriented")
print(given_str)

# e part
given_str="Python is a case sensitive language"
print(given_str.find("a"))

# f part
given_str=given_str.replace(" ","")
print(given_str)