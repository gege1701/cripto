# cripto
exercicios
def cal_root(y,p):
  b = 0
  for i in range(1,p-1):
    c = (i**2)-y
    if c % p == 0:
      b = 1
      return i
    else:
      i = i + 1
  #Quadratic Non-Residue  
  return -1

print(cal_root(14,29))
print(cal_root(6,29)) #answer
print(cal_root(11,29))
