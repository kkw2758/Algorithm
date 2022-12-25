# 2022/11/19 Baek 2805

N, M = map(int, input().split())
tree_height = list(map(int, input().split()))
tree_height.sort()

def parametric(start, end):
  global result

  while start <= end:
    mid = (start + end) // 2
    total_height = 0

    for i in range(N):
      if tree_height[i] > mid:
        total_height += tree_height[i] - mid

    if total_height >= M:
      result = mid
      start = mid + 1
    else:
      end = mid - 1

max_tree = tree_height[-1]
result = 0
parametric(1, max_tree)
print(result)