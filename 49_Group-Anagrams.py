class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for v in strs:
            tmp = "".join(sorted(v))
            if tmp in myDict: 
                myDict[tmp].append(v)
            else:
                myDict[tmp] = [v]
                
        ans = list(list())
        
        for key in myDict: 
            ans.append(myDict[key])
        
        return ans
    
