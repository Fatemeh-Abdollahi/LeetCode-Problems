class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        openingchar = []
        elements = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in elements.values():  
                openingchar.append(char)
            elif char in elements:  
                if openingchar and openingchar[-1] == elements[char]:
                    openingchar.pop()
                else:
                    return False

        return not openingchar

