import dsmlib

# A = 5
# B = 6
# dsmlib.write("A",A)
# dsmlib.write("B", B)

# dsmlib.checkloop()

# A = dsmlib.read("A")
# B = dsmlib.read("B")

# print(A+B)

# dsmlib.script_end()

dsmlib.write("A", 200)
A = 200
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)

# dsmlib.checkloop()

B = B - 15
C = C - 15

dsmlib.write("B",B)
dsmlib.write("C",C)


A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)
# dsmlib.checkloop()

C = C - 100
dsmlib.write("C",C)

A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)
# dsmlib.checkloop()


dsmlib.script_end()