import dsmlib


dsmlib.write("B", 200)
A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)


B = B - 15
dsmlib.write("B",B)

A = dsmlib.read("A")




dsmlib.checkloop()

A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)

dsmlib.script_end()