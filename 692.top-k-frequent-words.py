#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
      dic = {}
      for i in words:
        if i not in dic:
          dic[i]=0
        elif i in words:
          dic[i]+=1
      x = sorted(dic)
      x = sorted(dic.items(), key=lambda i:i[1],reverse=True)
      
      final = []
      for i in range(k):
        final.append(x[i][0])
      
      return final    
# @lc code=end

