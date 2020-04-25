n,m = map(int,input().split())
q = int(input())
for _ in range(q):
    a,b = map(int,input().split())
    l = b
    r = m-b+1
    u = a
    d = n-a+1
    ans = min(l,min(r,min(u,d)))
    a = ans%2
    ans = max(1,(ans+a)//2)
    print(ans)
