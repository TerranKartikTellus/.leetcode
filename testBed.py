def s(words,k):
  dic = {}
  for i in words:
    if i not in dic:
      dic[i]=0
    elif i in words:
      dic[i]+=1
  
  

  x = sorted(dic.items(), key=lambda i:i[1],reverse=True)
  print(x)
  x = sorted(dic)
  print(x)
  final = []
  for i in range(k):
    final.append(x[i][0])

  print(final)  
  return final





s(["i","love","leetcode","i","love","coding"],3)