from glob import glob


x = "x global variable"
y = "y global variable"
def fun():
    global y
    x = "x local variable"
    y = "y local variable"
    print("Inside Function")
    print(x)
    print(y)

fun()

print("\n=================\n")
print("Outside Function")

print(x)
print(y)
