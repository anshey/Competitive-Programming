#simple_array_sum
#complex_method

#a very big sum

n = int(input())
a = list(map(int,input().split()))
answer = 0
for i in range(len(a)):
    answer += a[i]
print(answer)