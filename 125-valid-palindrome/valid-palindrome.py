class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = ""
        for let in s:
            if let.isalnum():
                arr += let.lower()
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:  
                return False
                break
            left += 1
            right -= 1
        else:
            return True

        