#There are different data types in python.
def head(title):
    print("\n========= " + title + " ========\n")


#built in data types

################ String (str) ################
head("str")
x = "sample string"

print("x : ", type(x))
y = 123
print("y : ", type(y))
y = str(y)
print("y again : ", type(y))


############### Integer (int) #################
head("int")
x = 12

print(type(x))

x = "12"
print(type(x))

x = int(x)
print(type(x))


################ Float (float) ###############
head("float")

x=12.25

print(type(x))

x = "12.25"

print(type(x))

x = float(x)

print(type(x))

################ Complex (complex) ###############
head("complex")

x=complex(5,7)
print(x)
print(type(x))

x = "1+9j"
x = complex(x)
print(x)
print(type(x))

##############  Boolean (bool) ##################
head("bool")

x = bool(1)
print(x)
print(type(x))

x = False
print(type(x))

x = bool("False")
print(type(x))


############# bytes #############
head("bytes")

x = bytes(5)

print(x)
print(type(x))

########### btyearray ############

head("bytearray")

x = bytearray(5)

print(x)
print(type(x))

################## memoryview ###############
head("memoryview")

x = memoryview(bytes(1))
print(x)
print(type(x))
