n=int(input())
for i in range(1,n+1):
    #print(i,end=" ")
    a=list(map(int,input().strip().split()))[:n]
    print(a)