"""
Last updated by Rao on 29 Jan, 2017
"""
s = 100
myfile = "browsing.txt"
f = open(myfile, 'r')

# pass 1
C1 = {}
for l in f:
    items = l.strip().split(" ")
    for item in items:
        if item in C1:
            C1[item] = C1[item] + 1
        else:
            C1[item] = 1

L1 = {}
for item in C1:
    if C1[item] > s:
        L1[item] = C1[item]

# pass 2
f.seek(0)
C2 = {}
for l in f:
    items = l.strip().split(" ")
    for i in xrange(len(items)):
        for j in xrange(i + 1, len(items)):
            if (items[i] in L1) and (items[j] in L1):
                if items[i] < items[j]:
                    key = (items[i], items[j])
                else:
                    key = (items[j], items[i])
                if key in C2:
                    C2[key] = C2[key] + 1
                else:
                    C2[key] = 1

L2 = {}
for key in C2:
    if C2[key] > s:
        L2[key] = C2[key]

listL2 = []
for key, val in L2.items():
    newKeyA = key[0]
    newKeyB = key[1]
    prob = val / (1.0 * L1[newKeyA])
    listL2.append((newKeyA, prob, newKeyB))
    prob = val / (1.0 * L1[newKeyB])
    listL2.append((newKeyB, prob, newKeyA))

print "checkpoint ===="

sortListL2 = sorted(listL2, key=lambda x:x[1], reverse = True)
for i in xrange(5):
    print str(sortListL2[i][0]) + " -> " + str(sortListL2[i][2]) + " : " + str(sortListL2[i][1])

# pass 3
f.seek(0)
C3 = {}
for l in f:
    items = l.strip().split(" ")
    for i in xrange(len(items)):
        for j in xrange(i + 1, len(items)):
            for k in xrange(j + 1, len(items)):
                if items[i] <= items[j] <= items[k]:
                    pair1 = (items[i], items[j])
                    pair2 = (items[i], items[k])
                    pair3 = (items[j], items[k])
                    if (pair1 in L2) and (pair2 in L2) and (pair3 in L2):
                        key = (items[i], items[j], items[k])
                        if key in C3:
                            C3[key] = C3[key] + 1
                        else:
                            C3[key] = 1
                elif items[i] <= items[k] <= items[j]:
                    pair1 = (items[i], items[k])
                    pair2 = (items[i], items[j])
                    pair3 = (items[k], items[j])
                    if (pair1 in L2) and (pair2 in L2) and (pair3 in L2):
                        key = (items[i], items[k], items[j])
                        if key in C3:
                            C3[key] = C3[key] + 1
                        else:
                            C3[key] = 1
                elif items[k] <= items[i] <= items[j]:
                    pair1 = (items[k], items[i])
                    pair2 = (items[k], items[j])
                    pair3 = (items[i], items[j])
                    if (pair1 in L2) and (pair2 in L2) and (pair3 in L2):
                        key = (items[k], items[i], items[j])
                        if key in C3:
                            C3[key] = C3[key] + 1
                        else:
                            C3[key] = 1
                elif items[k] <= items[j] <= items[i]:
                    pair1 = (items[k], items[j])
                    pair2 = (items[k], items[i])
                    pair3 = (items[j], items[i])
                    if (pair1 in L2) and (pair2 in L2) and (pair3 in L2):
                        key = (items[k], items[j], items[i])
                        if key in C3:
                            C3[key] = C3[key] + 1
                        else:
                            C3[key] = 1
                elif items[j] <= items[i] <= items[k]:
                    pair1 = (items[j], items[i])
                    pair2 = (items[j], items[k])
                    pair3 = (items[i], items[k])
                    if (pair1 in L2) and (pair2 in L2) and (pair3 in L2):
                        key = (items[j], items[i], items[k])
                        if key in C3:
                            C3[key] = C3[key] + 1
                        else:
                            C3[key] = 1
                elif items[j] <= items[k] <= items[i]:
                    pair1 = (items[j], items[k])
                    pair2 = (items[j], items[i])
                    pair3 = (items[k], items[i])
                    if (pair1 in L2) and (pair2 in L2) and (pair3 in L2):
                        key = (items[j], items[k], items[i])
                        if key in C3:
                            C3[key] = C3[key] + 1
                        else:
                            C3[key] = 1
                else:
                    raise Exception("Wrong !")

L3 = {}
for key in C3:
    if C3[key] > s:
        L3[key] = C3[key]

listL3 = []
for key, val in L3.items():
    newKeyA = (key[0], key[1])
    prob = val / (1.0 * L2[newKeyA])
    listL3.append((newKeyA, prob, key[2]))
    newKeyB = (key[0], key[2])
    prob = val / (1.0 * L2[newKeyB])
    listL3.append((newKeyB, prob, key[1]))
    newKeyC = (key[1], key[2])
    prob = val / (1.0 * L2[newKeyC])
    listL3.append((newKeyC, prob, key[0]))

def mycmp(o1, o2):
    if o1[1] != o2[1]:
        return cmp(o1[1], o2[1])
    else:
        return cmp(o2[0], o1[0])

print ""
print "checkpoint ===="
sortListL3 = sorted(listL3, cmp = lambda x, y : mycmp(x, y), reverse = True)
for i in xrange(5):
    print str(sortListL3[i][0]) + " -> " + str(sortListL3[i][2]) + " : " + str(sortListL3[i][1])