class Solution:
    def segregateElements(self, arr):
        # Create an empty list of the same length as arr
        arr2 = [None for _ in range(len(arr))]

        # Initialize counters for positive and negative numbers
        count0 = count1 = 0

        # Count positive and negative numbers
        for i in range(len(arr)):
            if arr[i] >= 0:
                count0 += 1
            elif arr[i] < 0:
                count1 += 1

        # Start index for placing negative numbers
        start = count0

        # Place positive numbers in the beginning of arr2
        s = 0
        for i in range(len(arr)):
            if arr[i] >= 0:
                arr2[s] = arr[i]
                s += 1

        # Place negative numbers after the positive numbers
        for i in range(len(arr)):
            if arr[i] < 0:
                arr2[start] = arr[i]
                start += 1

        for i in range(len(arr)):
            arr[i] = arr2[i]



arr = [3,5,8,-4,-1,8,7,-3]

solution = Solution()
solution.segregateElements(arr)
print("Array with negative elements at one side is ",arr)