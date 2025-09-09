"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    # Base Case:
    if x <= 1:
        return x
    # Recursive Case:
    else:
        return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
    # Initialize variables which will store the current run and the largest run
    largest_run = 0
    curr_run = 0

    for element in mylist:
        # Adds to curr_run if element matches key
        if element == key:
            curr_run += 1
        # Saves run counter if it's the longest so far and then resets curr_run counter if element doesn't matches key
        else:
            if curr_run > largest_run:
                largest_run = curr_run
            curr_run = 0
    # After going through the whole list, double check if the curr_run is bigger than largest_run
    if curr_run > largest_run:
        largest_run = curr_run

    return largest_run


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    ### TODO
    pass



