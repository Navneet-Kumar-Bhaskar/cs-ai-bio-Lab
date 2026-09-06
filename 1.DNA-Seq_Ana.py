b = False

while b == False:
        a = input("Enter the DNA Sequence: ").upper()
        b = True

        if len(a) == 0:
                b = False
        else:
                for x in a:
                        if x != "A" and x != "T" and x != "C" and x != "G":
                                b = False

        if b:
                print("The DNA sequence is valid.")
        else:
                print("The DNA sequence is invalid. Please try again.")

d1 = 0
d2 = 0
d3 = 0
d4 = 0

for x in a:
        if x == "A":
                d1 += 1
        elif x == "T":
                d2 += 1
        elif x == "C":
                d3 += 1
        elif x == "G":
                d4 += 1

print("The number of Adenine (A) is: ", d1)
print("The number of Thymine (T) is: ", d2)
print("The number of Cytosine (C) is: ", d3)
print("The number of Guanine (G) is: ", d4)
