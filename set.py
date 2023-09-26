#declaring variables and assigning to set values
# joining one set with another
x = {1,2,3,4,5}
y = {6,7,8,9}
z = {1,10,12,14}
w = x.union(y)
t = x | y
b = x.intersection(z)

#union
print(w)
print(t)

#finding intersection values
print(b)

#substraction
a = y - x
print(a)