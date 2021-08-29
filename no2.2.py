"""
2.2
"""
print ("a.")
for p in True, False:
    for q in True, False:
        if ((p and q) and p) or (not (p and q)) == False:
            print ("INVALID! when p =", p, "and q =", q)

print ("\nb.")        
for p in True, False:
    for q in True, False:
        if (p and (p or q)) or (not p) == False:
            print ("INVALID! when p =", p, "and q =", q)

print ("\nc.")        
for p in True, False:
    for q in True, False:
        if (((p or q) and (not p)) and q) or (not ((p or q) and (not p))) == False:
            print ("INVALID! when p =", p, "and q =", q)

print ("\nd.")        
for p in True, False:
    for q in True, False:
        for r in True, False:
            for s in True, False:
                a = ((p and q) or (not p)) and ((r and s) or (not r)) and (p or r)
                b = q or s
                if ((a and b) or (not b)) == False:
                    print ("INVALID! when p =", p, ", q =", q, ", r =", r, ", and s =", s)

print ("\ne.")
for p in True, False:
    for q in True, False:
        for r in True, False:
            for s in True, False:
                a = ((p and q) or (not p)) and ((r and s) or (not r)) and ((not q) or (not s))
                b = (not p) or (not r)
                if ((a and b) or (not b)) == False:
                    print ("INVALID! when p =", p, ", q =", q, ", r =", r, ", and s =", s)