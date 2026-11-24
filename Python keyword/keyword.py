# -------->  Control flow  <---------
x = 6
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Less")

# -------->  Function  <---------
def my_function():
    return "Hello"

# -------->  Class  <---------
class MyClass:
    pass

# -------->  Exception Handling  <---------
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup")

# -------->  Content Manager  <---------
with open("keyword.py", "r") as f:
    content = f.read()


