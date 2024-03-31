def are_vampire_fangs_variety(x, y):
    """
    A variation of the vampire fangs check that allows both fangs to end with zero.
    This function checks if the multiplication of x and y results in a number that
    can be formed by rearranging the digits of x and y, without the restriction that
    fangs cannot both end in zero.
    """
    # Calculate the product of x and y
    v = x * y
    # Convert the numbers to strings for digit manipulation
    str_v, str_x, str_y = str(v), str(x), str(y)
    
    # Prepare the combined sorted list of digits from the fangs
    sorted_fangs = sorted(str_x + str_y)
    # Prepare the sorted list of digits from the original number
    sorted_v = sorted(str_v)
    
    # Check if the sorted digits of the fangs and the original number match
    return sorted_fangs == sorted_v

# Example tests
examples = [(20, 50), (210, 600), (30, 51), (222, 666)]
results = {f'{x} x {y}': are_vampire_fangs_variety(x, y) for x, y in examples}
results
