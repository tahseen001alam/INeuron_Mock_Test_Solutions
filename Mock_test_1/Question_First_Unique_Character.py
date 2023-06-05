s=input()
ls=list(s)
kt=0
for i in range(len(ls)):
    if ls.count(ls[i])==1:
        print(i)
        kt=1
        break
if kt==0:
    print(-1)
