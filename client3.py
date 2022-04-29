import dsmlib


dsmlib.write("C", 100)
A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)


A = A - 30
dsmlib.write("A",A)


dsmlib.checkloop()

A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)

dsmlib.script_end()
