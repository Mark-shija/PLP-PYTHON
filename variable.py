num = 10
num1 = num2 = 100
print(num2)

num2 = 'Now contain string';
print(num2);

a = b = c = 100
print(a, b, c)

type(num2)
# Output: <class 'str'>

print(type(num2))

# GARBAGE ALLOCATION OF MEMORY
# consider

a  = b = 300
b = 200
a = 400
print("Memory Address of a : ", id(a))
print("Memory Address of b : ", id(b))

# we lost access to 300 object

