def sm(x,y,n):
    if n ==0:
        return x
    else:
        return y+sm(x,y,n-1)
   print(sm(2,4,3)) 