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

dsmlib.write("A", 15)

dsmlib.checkloop()

dsmlib.write("A",100)

dsmlib.checkloop()

print(dsmlib.read("A"))

dsmlib.checkloop()

print(dsmlib.read("A"))

dsmlib.checkloop()

dsmlib.script_end()