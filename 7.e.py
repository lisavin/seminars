def power(a, n):
    if n == 1:
        return (a)
    if n == 0:
        return(1)
    if n != 0 and n != 1:
        return (a*power(a, n-1))
a = int(input())
n = int(input())
print(power(a, n))
