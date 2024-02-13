t=int(input())
for _ in range(t):
    a=int(input())
    b=input()
    lst=[int(i) for i in b]
    d={0:1}
    run=[]
    summ=0
    for i in lst:
        summ+=i
        run.append(summ)
    ans=0
    for i in range(len(lst)):
        z=run[i]-(i+1)
        if z in d:
            ans+=d[z]
        d[z]=d.get(z,0)+1
    print(ans)