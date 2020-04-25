n, m = input().split()
temp = n
n = str(n)
m = int(m)
sm = 0
s = ''
for i in n:
    sm = sm + int(i)
for i in range(0, len(n)):
  #  print(s)
    if(m > 1 and n[i] != '9'):
        sm = sm - int(n[i])
        sm = sm + 9
        m = m - 1
        s = s + '9'
    elif (m > 0):
        r = 9 - ((sm - int(n[i]) + 9)%3)
        if(r > int(n[i]) or i == len(n) - 1):
            s = s + str(r)
            m = m - 1
            continue
        s = s + n[i]
    else:
        s = s + n[i]
print(s)
