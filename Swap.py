def ReadandWriteDATA():
    A = input("Tell the name of File 1: ")
    B = input("Tell the name of File 2: ")
    A1 = open(A)
    B1 = open(B)
    A_read = A1.read()
    B_read = B1.read()
    A1.close()
    B1.close()

    A2 = open(A,"w")
    B2 = open(B,"w")

    A2.write(B_read)
    B2.write(A_read)

    A2.close()
    B2.close()

    print("Data in your Files has been swapped Succesfully!!!")

ReadandWriteDATA()

print("Method2\n")

with open("txt1", 'r') as A1:
    A_read = A1.read()
    print(A_read)