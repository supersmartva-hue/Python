# Variables & Data Types
# ---------> Swap two variables <----------
a, b = 10, 20
a, b = b, a
print(a, b)

# ---------> Check datatype <----------
x = input()
print(type(x))

# ---------> Convert float to int <----------
x = 10.5
print(int(x))

# ---------> Sum of two floats <----------
a = float(input())
b = float(input())
print(a + b)

# ---------> Multiple assignment <----------
a = b = c = 5
print(a, b, c)

#Operators
# ---------> Even or odd <----------
n = int(input())
print(n % 2 == 0)

# ---------> Largest of 3 <----------
print(max(1, 5, 3))

# ---------> Divisible by 5 and 11 <----------
n = int(input())
print(n % 5 == 0 and n % 11 == 0)

# ---------> Power <----------
print(2 ** 3)

# ---------> Bitwise AND <----------
print(5 & 3)


# Built-in Functions
# ---------> Length <----------
print(len('hello'))

# ---------> Sum <----------
print(sum([1, 2, 3]))

# ---------> Max <----------
print(max([1, 5, 3]))

# ---------> Sort <----------
print(sorted([3, 1, 2]))

# ---------> Type casting <----------
print(str(10))



#Control Flow
# ---------> Positive or negative <----------
n = int(input())
print('Positive' if n > 0 else 'Negative')

# ---------> Grade <----------
marks = 80
print('A' if marks >= 75 else 'B')

# ---------> Leap year <----------
year = 2024
print(year % 4 == 0)

# ---------> Nested if <----------
x = 10
if x > 5:
    if x < 15:
        print('OK')

# ---------> Vowel check <----------
ch = 'a'
print(ch in 'aeiou')


# Loops
# ---------> Print 1-10 <----------
for i in range(1, 11):
    print(i)

# ---------> Sum n numbers <----------
n = 5
print(sum(range(1, n + 1)))

# ---------> Reverse number <----------
n = 123
print(str(n)[::-1])

# ---------> Factorial <----------
f = 1
for i in range(1, 6):
    f *= i
print(f)

# ---------> While loop <----------
i = 1
while i <= 5:
    print(i)
    i += 1



#Functions
# ---------> Simple function <----------
def f():
    print('Hi')

f()

# ---------> Add function <----------
def add(a, b):
    return a + b

print(add(2, 3))

# ---------> Default argument <----------
def f(x=10):
    print(x)

f()


#Strings
# ---------> Reverse string <----------
s = 'hello'
print(s[::-1])

# ---------> Uppercase <----------
print('hi'.upper())

# ---------> Palindrome <----------
s = 'madam'
print(s == s[::-1])

# ---------> Replace <----------
print('hi'.replace('h', 'y'))


#Lists
# ---------> Append <----------
l = [1, 2]
l.append(3)

# ---------> Remove <----------
l = [1, 2, 3]
l.remove(2)
print(l)

# ---------> Max <----------
print(max([1, 5, 3]))

# ---------> Reverse <----------
l = [1, 2, 3]
l.reverse()
print(l)


#Tuples
# ---------> Create tuple <----------
t = (1, 2, 3)

# ---------> Access <----------
print(t[1])

# ---------> Count <----------
print(t.count(2))

# ---------> Convert <----------
tuple([1, 2])

# ---------> Unpacking <----------
a, b = (1, 2)



# Dictionary

# ---------> Create <----------
d = {'a': 1}

# ---------> Access <----------
print(d['a'])

# ---------> Add key <----------
d['b'] = 2

# ---------> Loop <----------
for k, v in d.items():
    print(k, v)

# ---------> Get <----------
print(d.get('a'))




# Set
# ---------> Create <----------
s = {1, 2, 3}

# ---------> Add <----------
s.add(4)

# ---------> Remove <----------
s.remove(2)

# ---------> Union <----------
print({1, 2} | {2, 3})

# ---------> Intersection <----------
print({1, 2} & {2, 3})