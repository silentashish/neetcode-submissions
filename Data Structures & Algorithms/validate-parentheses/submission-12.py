class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for item in s:
            if item in p_map:
                stack.append(item)
            else:
                if not stack:
                    return False
                
                if p_map[stack.pop()] != item:
                    return False
        return len(stack) == 0
        