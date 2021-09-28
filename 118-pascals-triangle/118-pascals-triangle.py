class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas = [[1]]
        
        for i in range(numRows-1):
            temp = [0] + pas[-1] + [0]
            arr = []
            for j in range(len(pas[-1])+1):
                arr.append(temp[j]+temp[j+1])
            pas.append(arr)
        return pas
