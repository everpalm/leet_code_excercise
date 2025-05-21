'''
To simplify xml validator, use 1 capital character for begin-tag and small case for end-tag.
Eg. AABbCcaa is a valid string.  Please write this string validator in python.
CAABbCBbcaac -> valid
ABCccba -> invalid
bAaB -> invalid
AABBCbcbaa -> invalid
'''
class Solution:
    def is_valid_xml_string(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch.isupper():  # Begin-tag
                stack.append(ch)
            elif ch.islower():  # End-tag
                if not stack:
                    return False  # No tag to close
                top = stack.pop()
                if ch != top.lower():
                    return False  # Mismatched tag
            else:
                return False  # Invalid character

        return len(stack) == 0  # All tags must be closed

if __name__ == '__main__':
    sol = Solution()
    my_string = 'CAABbCBbcaac'
    print('Example 1 = ', sol.is_valid_xml_string(my_string))  # Expected True

    my_string = 'ABCccba'
    print('Example 2 = ', sol.is_valid_xml_string(my_string))  # Expected False

    my_string = 'bAaB'
    print('Example 3 = ', sol.is_valid_xml_string(my_string))  # Expected False

    my_string = 'AABBCbcbaa'
    print('Example 4 = ', sol.is_valid_xml_string(my_string))  # Expected False