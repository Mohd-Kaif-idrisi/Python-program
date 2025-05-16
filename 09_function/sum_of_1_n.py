def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum+= i
    return sum

ans = sum(10)
print(ans)