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


print(dsmlib.read("A"))

dsmlib.checkloop()

dsmlib.write("A", 15)

dsmlib.checkloop()

print(dsmlib.read("A"))

dsmlib.checkloop()

dsmlib.write("A",100)

dsmlib.checkloop()

print(dsmlib.read("A"))

dsmlib.checkloop()

dsmlib.script_end()
