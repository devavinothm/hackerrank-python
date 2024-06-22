

n, m = map(int, input().split())
atheles = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
[print(*x) for x in sorted(atheles, key=lambda x: x[k])]
