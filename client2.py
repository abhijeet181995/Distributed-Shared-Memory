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




dsmlib.write("A", 25)

dsmlib.checkloop()

print(dsmlib.read("A"))

dsmlib.checkloop()

print(dsmlib.read("A"))

dsmlib.checkloop()

dsmlib.write("A",100)

dsmlib.checkloop()

print(dsmlib.read("A"))

dsmlib.checkloop()

print(dsmlib.read("A"))

dsmlib.checkloop()

dsmlib.script_end()