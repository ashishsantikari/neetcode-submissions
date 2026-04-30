class Solution:
    def isValid(self, str: str) -> bool:
        stack = []
        pairs = {"}": "{", "]": "[", ")": "("}
        i = 0
        while i < len(str):
            c = str[i]
            if len(stack) > 0 and c in pairs and pairs[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
            i += 1

        if len(stack) > 0:
            return False

        return True
