def power(b,e):
    if e==0:
        return 1
    x=power(b,e//2)%107
    if e%2!=0:
        return (x*x*b)%107
    else:
        return (x*x)%107
    
a,b=map(int,input().split())
print(power(a,b))



