# modulus dan floor division
# %=, //=
a = 5
print("nilai a = ", a)

a %= 5 # artinya a = a % 5
print("nilai a % 5,nilai a menjadi =", a)

a //= 5 # artinya a = a // 5
print("nilai a / 5,nilai a menjadi =", a)

a **= 5 # artinya a = a ** 5
print("nilai a ** 5,nilai a menjadi =", a)

# OR
c = True
print("nilai c = ", c)
c |= False #artinya c = c or False
print("nilai c | 5,nilai a menjadi =", c)
c |= True #artinya c = c or True
print("nilai c | 5,nilai a menjadi =", c)

#AND
c = True
print("nilai c = ", c)
c &= False #artinya c = c or False
print("nilai c & 5,nilai a menjadi =", c)
c |= True #artinya c = c or True
print("nilai c & 5,nilai a menjadi =", c)