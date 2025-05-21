'''
Check if a json dictionary has a given value (cannot use json.dump)
Input: data = {'a':{'b': None,'c':'3', 'd':3}}, value = 3 => yes
Input: data = {'a':{'b':2,'c':[3,4,5]}}, value = 3 => yes
Input: data = {'a':[{'b':2},{3:'c'}]}, value = 3 => yes
Input: data = {'a':{'b':2,'c':3}}, value = 4 => no
Input: data = {'a':{'b':None}}, value = None => yes
'''
class Solution():
    def has_value(self, data, target):
        if isinstance(data, dict):
            for key, val in data.items():
                if self.has_value(val, target) or key == value:
                    return True
        elif isinstance(data, list):
            for item in data:
                if self.has_value(item, target):
                    return True
        else:
            return data == target
        return False
    
    def has_helper(self, data, target):
        def helper(node):
            if isinstance(node, dict):
                for key, val in node.items():
                    if key == value: 
                        return True
                    if helper(val):
                        return True
                
            elif isinstance(node, list):
                for item in node:
                    if helper(item):
                        return True
            else:
                return node == target
            return False

        return helper(data)
    
if __name__ == '__main__':
    sol = Solution()
    data = {'a':{'b': None,'c':'3', 'd':3}}
    # data = {‘a’:{‘b’:None,’c’:’3’, ‘d’:3}}
    value = 3

    print('Example 1 = ', sol.has_value(data, value))  # Expected yes

    data = {'a':{'b':2,'c':[3,4,5]}}
    value = 3
    print('Example 2 = ', sol.has_value(data, value))  # Expected yes

    data = {'a':[{'b':2},{3:'c'}]}
    value = 3
    print('Example 3 = ', sol.has_value(data, value))  # Expected yes
    print('Example 3-1 = ', sol.has_helper(data, value))  # Expected yes
    
    data = {'a':{'b':2,'c':3}}
    value = 4 
    print('Example 4 = ', sol.has_value(data, value))  # Expected no
    
    data = {'a':{'b':None}}
    value = None
    print('Example 5 = ', sol.has_value(data, value))   # Expected yes 