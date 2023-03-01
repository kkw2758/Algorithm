# 2023/03/01 Baek 4659

moum = ["a", "e", "i", "o", "u"]
def check_pwd(candidate_pwd):
  moum_cnt = 0
  before = ""
  before_moum = 0
  before_jaum = 0

  for i in candidate_pwd:
    if i in moum:
      moum_cnt += 1
      before_moum += 1
      before_jaum = 0
    else:
      before_moum = 0
      before_jaum += 1

    if before_moum >= 3 or before_jaum >= 3:
      return False

    if before != i:
      before = i
    else:
      if before not in ["e", "o"]:
        return False
  
  if moum_cnt == 0:
    return False

  return True
  

while True:
  candidate_pwd = input()
  if candidate_pwd == "end":
    break
  if check_pwd(candidate_pwd):
    print("<{}> is acceptable.".format(candidate_pwd))
  else:
    print("<{}> is not acceptable.".format(candidate_pwd))