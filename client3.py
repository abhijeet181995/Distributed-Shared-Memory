import dsmlib

# A = dsmlib.read("A")
# B = dsmlib.read("B")

# A = A - 10
# B = B + 10

# dsmlib.write("A",A)
# dsmlib.write("B", B)

# dsmlib.checkloop()

# A = dsmlib.read("A")
# B = dsmlib.read("B") 


# A = A - 5
# B = B + 5


# dsmlib.write("A",A)
# dsmlib.write("B", B)

# dsmlib.checkloop()

# A = dsmlib.read("A")
# B = dsmlib.read("B")

# dsmlib.checkloop()

# print(A+B)


# dsmlib.script_end()

dsmlib.write("C", 100)
A = dsmlib.read("A")
B = dsmlib.read("B")
C = 100
print("sum=",A+B+C)

# dsmlib.checkloop()

A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)
# dsmlib.checkloop()


B = B+200
dsmlib.write("B",B)

A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)
# dsmlib.checkloop()

dsmlib.script_end()
