import dsmlib

dsmlib.write("A", 200)
A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)


C = C - 15
dsmlib.write("C",C)



dsmlib.checkloop()

A = dsmlib.read("A")
B = dsmlib.read("B")
C = dsmlib.read("C")
print("sum=",A+B+C)

dsmlib.script_end()