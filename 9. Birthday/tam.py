c = "T"

#for i in range(1, 3):
#    print(c*24)
#for i in range(1, 10):
#    print((c*5).center(23, " "))

T = [
    "TTTTTTTTTTTTTTTTTTT", 
    "        TTT        ",
    "        TTT        ",
    "        TTT        ",
    "        TTT        ",
    "        TTT        ",
    "        TTT        ",
]
A = [
    "    AA      ",
    "   AAAA     ",
    "  AA  AA    ",
    " AAAAAAAA   ",
    "AA      AA  ",
    "AA      AA  ",
]
M = [
    "MM      MM",
    "MMM    MMM",
    "MM MM MM M",
    "MM  MMM  M",
    "MM       M",
    "MM       M",
]
C = [
    "  CCCCCCCCC ",
    " CC         ",
    " CC         ",
    " CC         ",
    " CC         ",
    "  CCCCCCCCC "
]
U = [
    "UU       UU",
    "UU       UU",
    "UU       UU",
    "UU       UU",
    "UU       UU",
    " UUUUUUUU "
]
B = [
    "BBBBBBBBBB ",
    "BB      BB ",
    "BB      BB ",
    "BBBBBBBBBB ",
    "BB      BB ",
    "BB      BB ",
    "BBBBBBBBBB "
]
E = [
    "EEEEEEEEEEE",
    "EE         ",
    "EE         ",
    "EEEEEEEE   ",
    "EE         ",
    "EE         ",
    "EEEEEEEEEEE"
]

for i in range(len(A)):
    print(T[i] + "   " + A[i] + "   " + M[i])
for i in range(len(C)):
    print(C[i] + "   " + U[i])
for i in range(len(B)):
    print(B[i] + "   " + E[i])

##
