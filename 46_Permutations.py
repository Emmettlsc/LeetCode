class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, cur): 
            if i == len(nums): 
                res.append(cur.copy())
                return
            
            for n in nums: 
                if n not in cur: 
                    cur.append(n)
                    dfs(i+1, cur)
                    cur.pop()
        dfs(0, [])
        return res
