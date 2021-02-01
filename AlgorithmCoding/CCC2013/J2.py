sign=input()

ok = ["I", "O", "S", "H", "Z", "X", "N"]
o = "YES"
for i in range(len(sign)):
    if sign[i] not in ok:

        o = "NO"
        break

print(o)