class Solution:
    def sort012(self, arr, n):
        count0 = count1 = count2 = 0
        # code here
        for num in arr:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            elif num == 2:
                count2 += 1

        # Overwrite the array with 0s, 1s, and 2s in sorted order
        index = 0
        for _ in range(count0):
            arr[index] = 0
            index += 1
        for _ in range(count1):
            arr[index] = 1
            index += 1
        for _ in range(count2):
            arr[index] = 2
            index += 1

arr = [0,2,2,2,1,2,1,2,0,0,0]
n=len(arr)
solution = Solution()
solution.sort012(arr,n)
print("The sorted array is as : ")

print(arr)