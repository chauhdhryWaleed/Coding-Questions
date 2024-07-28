
from typing import List



class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        # code here
        
        result = []

        k=0
        arr.sort()
        # Calculate the sum of the first `n` elements
        for i in range(n-1):
            if arr[i]==arr[i+1]:
                k=1
                result.append(arr[i])
        if k==0:
            result.append(-1)
            
        r=set(result)
        return r

sol=Solution()

list=[1,2,2,3,4,5,6]

n=len(list)
print(sol.duplicates(n,list))