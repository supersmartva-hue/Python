print("Hello world, Nadia Mahak")
name = "Mahak"
age = 20
print(name, age)
print(type(name))
print(type(age))

cgpa = 3.36
isStudent = True
print(type(isStudent))


name = input("Enter your name: ")
print("Hello " + name)   #concatenation

# Type casting
age = input("Enter your age: ")
print(type(age)) 
print(age)

new_age = int(age) + 2
print(new_age)


product_1 = int(input("Enter value product 1: "))
product_2 = int(input("Enter value product 2: "))
product_3 = int(input("Enter value product 3: "))
Total = ( product_1 + product_2 + product_3)
print("Total Bill Amount: ", Total)

avg = Total/3 
print(avg)