from utils import hermite_generating

for n in range(6):
    coeffs = hermite_generating(n)
    print("H_" + str(n) + " = ", end="")
    for i, c in reversed(list(enumerate(coeffs))):
        print((((" + " if i != n else "") + str(c) + "x^" + str(i)) if c != 0 else ""), end="")
    print("")
        