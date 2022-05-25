# 1 => strings are array
str = "abc123"

print(str[3])


for x in str:
    print(x)

# concatination in string use +

str = str + "xyz"

# find lenth of string
length = len(x)



# find string in another string. find chunk of characters

if "bc" in str:
    print("bc find in " + x)

# chunk not present in string

if "bc14" not in str:
    print("bc14 not found")



# substring from a string or string slicing 

substr = str[1:4]
substr = str[:4]
substr = str[1:]
substr = str[:-4]
substr = str[-1:]
print("substr : "+substr)


# remove white spaces from start and end

strip = substr.strip()


# convert to lower case

lower = str.lower()

# convert to upper case

upper = str.upper()

# capitalize a string

str.capitalize()


# string replace
str.replace("find","with")


# string split  this will return an array.

str.split(",")


# Centered string str.center(length, char)
str.center(20,'#')

# find no of occurances in string

str.count(substr)

# endswith check whether string end on specific substring, return true/false

str.endswith(substr)

# expand tabs .. convert special char \t to spaces

str.expandtabs(3)

# find index of a substirng this will return index

x = str.find(substr)
