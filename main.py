from itertools import combinations


def rSubset(arr, r):
    return list(combinations(arr, r))


print("Algorithm 1")
initial = input("Enter set of x: ")  # 0, 6, 9, 10, 11, 12, 15
initial = initial.split(',')
x = list(map(int, initial))
# Complete Digest
comDeltaX = []
for i in range(len(x) - 1):
    diff = x[i + 1] - x[i]
    comDeltaX.append(diff)
print("Complete Digest: ", sorted(comDeltaX))

# Partial Digest
parDeltaX = rSubset(x, 2)
newPar = []
for i, j in parDeltaX:
    newPar.append(abs(i-j))
print("Partial Digest: ", sorted(newPar), "\n")


# Partial Digest
def Delete(deltax, pos):
    for i in pos:
        deltax.remove(i)
    return deltax


def unique(deltax):
    uniqueList = list(set(deltax))
    return uniqueList


print("Algorithm 2")
deltaX = input("Enter the delta x set: ")  # [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 9, 9, 10, 11, 12, 15]
deltaX = deltaX.split(',')
deltaX = list(map(int, deltaX))

X = [0, max(deltaX)]
deltaX.remove(max(deltaX))
lenX = round(len(deltaX) / 2)
boolIn = True
uniDelta = unique(deltaX)

for i in range(lenX):
    if len(deltaX) == 0:
        X.sort()
        print("Partial Digest: ", X)
        break
    maxi = max(uniDelta)
    pos = []
    for j in X:
        pos.append(abs(maxi - j))
    for p in pos:
        if p not in deltaX:
            boolIn = False
            uniDelta.remove(maxi)
            break
    if boolIn:
        X.append(maxi)
        deltaX = Delete(deltaX, pos)
        uniDelta.remove(maxi)
    boolIn = True
