class Solution:
    # Function to return the count of number of elements in union of two arrays.
    def doUnion(self, arr1, arr2):
        arr3 = arr1 + arr2
        k = set(arr3)

        return len(k)



arr = [1,2,3,4,5,6]
arr1 = [4,5,6,7,8,9]
solution = Solution()
print("The number of elements in union of array 1 and array 2 are ",solution.doUnion(arr,arr1))
