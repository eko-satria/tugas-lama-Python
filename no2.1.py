for p in True, False:
        for r in True, False:
            for s in True, False:
                q = True
                x = (((not p) or r)) and (not s)
                y = (not r) and q
                a = ((not s) and y) or (not (not s))
                b = a and x
                c = q and b or not q
                print ( "q=", q, ", p=", p, ", r=", r, ", s=", s, ", result=", c)