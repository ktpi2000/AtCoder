# プロコン
ans = 0
for i in range(3):
    s1, e1 = map(int, input().split())
    ans += s1 * e1 / 10
print(int(ans))