def KMP_table(pattern):
  lp = len(pattern)
  tb = [0 for _ in range(lp)]

  pidx = 0
  for idx in range(1, lp):
    while pidx > 0 and pattern[idx] != pattern[pidx]:
      pidx = tb[pidx - 1]
    # if pattern[idx] != pattern[pidx]:
    #   pidx = 0
  
    if pattern[idx] == pattern[pidx]:
      pidx += 1
      tb[idx] = pidx

  return tb

pattern = "ABAABAB"
print(KMP_table(pattern))