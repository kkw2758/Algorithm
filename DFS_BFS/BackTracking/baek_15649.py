n, m = map(int, input().split())

def dfs(now, i):
    if i == 0:
        for i in now:
            print(i, end = ' ')
        print("")
    else:
        for x in range(n):
            if not((x + 1) in now):
                now.append(x + 1)
                dfs(now, i - 1)
                now.pop()

dfs([], m)