# silverkkang
print("이정도좆밥")
print("오늘 풀고 내일도 한문제 ㄱ")

n = int(input())

def factorial(n):
    k = 1
    for i in range(1, n+1):
        k = k*i
    return k

print(factorial(n))