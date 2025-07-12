n=int(input(""))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=int(input(""))
l=[]
m=[]
z=0
for i in range(0,n):
    for j in range(n):
        if d==a[i]+b[j]:
            l.append(a[i])
            m.append(b[j])
        elif a[i]+b[j]>d:
            k=a[i]+b[j]-d
            date=k*100
            if(date>z):
                date=z

              
        
print(date)
