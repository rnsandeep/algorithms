from collections import Counter

def permutation(s):
    if len(s) <= 1:
       return s

    newperms = []
    for c in range(len(s)):
        perm1 = permutation(s[:c] + s[c+1:])
        for d in perm1:
            for pos in range(len(s)-1):
                if d[:pos] + s[c] + d[pos:] not in newperms:
                    newperms.append(d[:pos] + s[c] + d[pos:])
    return newperms

s = 'abc'

perms = permutation(s)
print(len(perms))
print(Counter(perms))
