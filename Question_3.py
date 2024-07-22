class Solution:
    def kthSmallest(self, arr, k):
        length=len(arr)
        if k<length:
            arr.sort()
            return arr[k - 1]
        else:
            return None


arr = [10,12,98, 2, 3, 4]
solution = Solution()

print("The Kth min element of array is ", solution.kthSmallest(arr,2))