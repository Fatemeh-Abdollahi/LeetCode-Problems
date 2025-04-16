class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for index, character in enumerate(s):
            if character == 'I':
                if index+1 < len(s) and s[index+1] == 'V':
                    sum = sum + 4
                elif index+1 < len(s) and s[index+1] == 'X':
                    sum = sum + 9
                else:
                    sum = sum + 1
            elif character == 'V':
                if index == 0 or s[index-1] != 'I':
                    sum = sum + 5
            elif character == 'X':
                if index == 0 or s[index-1] != 'I':
                    if index+1 < len(s) and s[index+1] == 'L':
                        sum = sum + 40
                    elif index+1 < len(s) and s[index+1] == 'C':
                        sum = sum + 90
                    else:
                        sum = sum + 10
            elif character == 'L':
                if index == 0 or s[index-1] != 'X':
                    sum = sum + 50
            elif character == 'C':
                if index == 0 or s[index-1] != 'X':
                    if index+1 < len(s) and s[index+1] == 'D':
                        sum = sum + 400
                    elif index+1 < len(s) and s[index+1] == 'M':
                        sum = sum + 900
                    else:
                        sum = sum + 100
            elif character == 'D':
                if index == 0 or s[index-1] != 'C':
                    sum = sum + 500
            elif character == 'M':
                if index == 0 or s[index-1] != 'C':
                    sum = sum + 1000
        
        return sum
        