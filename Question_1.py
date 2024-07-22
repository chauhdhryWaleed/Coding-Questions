
class Solution:
    def reverseWord(self, str):
        length = len(str)
        str = list(str)  # Convert string to list for mutability
        for i in range(length // 2):
            character = str[i]
            str[i] = str[length - 1 - i]
            str[length - 1 - i] = character
        return ''.join(str)  # Convert list back to string


solution = Solution()
print(solution.reverseWord("Geeks"))
