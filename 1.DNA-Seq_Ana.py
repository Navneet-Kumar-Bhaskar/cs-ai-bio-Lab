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


# Percentage of required nucleotides
total = len(a)
nucleotides = input("Enter the nucleotides to calculate percentage (A, T, C, G) separated by space: ").upper().split()
l1 = []
for nucleotide in nucleotides:            #prevent from duplicates
        if nucleotide not in l1:
                l1.append(nucleotide)

n = 0
for _ in l1:
        if _ == "A":
                n += (d1/total)*100
        elif _ == "T":
                n += (d2/total)*100
        elif _ == "C":
                n += (d3/total)*100
        elif _ == "G":
                n += (d4/total)*100

print(f"Percentage of [{' , '.join(l1)}] is: {n:.2f}%")


# Reverse Complement of the DNA sequence
rv = ""
for x in a:
        if x == "A":
                rv += "T"
        elif x == "T":
                rv += "A"
        elif x == "C":
                rv += "G"
        elif x == "G":
                rv += "C"

print(f"Reverse Complement of the DNA sequence is: {rv}")

# DNA → mRNA Transcription
mRNA = ""
for x in a:
        if x == "A":
                mRNA += "U"
        elif x == "T":
                mRNA += "A"
        elif x == "C":
                mRNA += "G"
        elif x == "G":
                mRNA += "C"

print(f"mRNA sequence is: {mRNA}")

# Split mRNA into Codons{It is a group of 3 nucleotides in mRNA}
s = len(mRNA) % 3
if s != 0:
        for i in range(0, len(mRNA)-s, 3):
                for j in range(i, i + 3):
                        print(mRNA[j], end="")
                print(" ", end="")
        for r in range(len(mRNA)-s, len(mRNA)):
                print(mRNA[r], end="")


