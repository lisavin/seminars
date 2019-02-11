s = list(map(int , input().split()))
n = s[0]
m = s[1]

g = [[] for i in range(n)]

for i in range(m):
    s = list(map(int , input().split()))
    a = s[0] - 1
    b = s[1] - 1
    g[a].append(b)
    g[b].append(a)

component = [None] * n

for i in range(n):
    if component[i] is None:
        st = [i]
        component[i] = i
        while len(st) > 0:
           current = st.pop()
           for child in g[current]:
               if component[child] is None:
                   component[child] = i
                   st.append(child)


answer = [[] for i in range(n)] 
for i, comp in enumerate(component):
        answer[comp].append(i + 1)

answer = [i for i in answer if i != []]

answer.sort(key = len, reverse=True)

print(len(answer))
for i in answer:
    print(len(i))
    print(' '.join(map(str, sorted(i))))
