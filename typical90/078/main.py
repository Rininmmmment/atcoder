from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(m):
    ai, bi = map(int, input().split())
    d[ai].append(bi)
    d[bi].append(ai)

ans = 0
for i in range(1, n+1):
    # 計算量を抑えるならsortじゃなくてminのが良い
    first = second = float('inf')
    for num in d[i]:
        if num < first:
            second = first
            first = num
        elif num < second:
            second = num

    if (first < i and i < second):
        ans += 1

print(ans)