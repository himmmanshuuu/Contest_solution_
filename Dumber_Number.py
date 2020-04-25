import math 
def fun(a, b): 
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(fun(a,b))
