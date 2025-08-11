s = str(input())

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

alpha = []

for i in s:
    alpha.append(i)

for i in alphabet:
    print(alpha.count(i),end = '')