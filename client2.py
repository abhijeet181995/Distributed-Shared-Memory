import dsmlib

# A = dsmlib.read("A")
# B = dsmlib.read("B")

# A = A - 2
# B = B + 2

# dsmlib.write("A",A)
# dsmlib.write("B", B)

# dsmlib.checkloop()

# A = dsmlib.read("A")
# B = dsmlib.read("B")


# A = A - 5
# B = B + 2


# dsmlib.write("A",A)
# dsmlib.write("B", B)

# dsmlib.checkloop()

# A = dsmlib.read("A")
# B = dsmlib.read("B")


# print(A+B)


# dsmlib.script_end()

dsmlib.write("B", 200)

A = dsmlib.read("A")
B = 200
C = dsmlib.read("C")
print("sum=",A+B+C)

# dsmlib.checkloop()

A = A + 30

dsmlib.write("A",A)

A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)
# dsmlib.checkloop()


A = A - 100
dsmlib.write("A",A)

A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)
# dsmlib.checkloop()

dsmlib.script_end()