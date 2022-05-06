# method 1 
# this method prints true  or false 
string=input("Enter a string : \n \t")

print("name" in string)



# method 2 
# this method prints yes or no

newstring=input("Enter another string: \n \t ")

if "name" in newstring:
    print("yes name is present")
else:
    print("no name is not present ")