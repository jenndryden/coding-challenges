class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        def backtracking(left, right, count, cand):
            if left==right==0:
                answer.append(cand)
                return 
            if left > 0:
                backtracking(left - 1, right, count+1, cand+"(")
            if right > 0 and count > 0:
                backtracking(left,right-1,count-1, cand+")")
            
        backtracking(n,n,0,"")
        return answer