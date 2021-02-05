#diagonal difference
n = int(input())
mat = []
for i in range(n):
    t = list(map(int,input().split()))
    mat.append(t)

d1 = 0
d2 = 0
for i in range(n):
    d1 += mat[i][i]
    d2 += mat[i][n-1-i]
print(abs(d1-d2))