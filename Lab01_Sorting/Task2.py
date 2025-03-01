def Calculate(z):
    lst=z.split(" ")
    x=int(lst[1])
    op=lst[2]
    y=int(lst[3])
    if op=="+":
        return float(x+y)
    elif op=="-":
        return float(x-y)
    elif op=="*":
        return float(x*y)
    elif op=="/":
        return (x/y)
    
n=int(input())
for i in range(n):
    T=str(input())
    print(Calculate(T))
