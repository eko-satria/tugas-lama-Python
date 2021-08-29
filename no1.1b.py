for i1 in range(0,6):
    for i2 in range(0,6):
        for i3 in range(0,6):
            if i1 != i2 and i2 != i3 and i1 != i3:
                i4 = i1+1 + i2+1 + i3+1
                i5 = i4%2
                if i5 == 0:
                    print (i1+1, i2+1, i3+1)