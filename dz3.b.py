s=list(map(int, input().split()))
a=int(input())
s.append(a)
s.sort()
s.reverse()
if s.count(a)==1:
    print(s.index(a)+1)
if s.count(a)!=1:
    print(s.index(a)+s.count(a))

