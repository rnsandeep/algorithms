val1 = "Lernin Acdmy"
val2 = "Learning Academy"


def edit_dst(val1, val2):

    n = len(val1)
    q = len(val2)
    i = 0
    dst = 0
    while(i < n and i < q):
        if val1[i] == val2[i]:
            dst = edit_dst(val1[i+1:], val2[i+1:])
        else:
            dst = min(1 + edit_dst(val1[i+1:], val2[i+1:]), 1 + edit_dst(val1[i+1:], val2), 1+ edit_dst(val1, val2[i+1:]))
            #      change                                     cutting                           adding

    if n > q:
        dst = q-n + dst
    else:
        dst = n-q + dst

    return dst


final = edit_dst(val1, val2)
print(final)


    


