import doctest

class Solution:
    cache = []
    def __init__(self, *args):
        self.args = *args

        
def short(*args):
    """
    >>> s = [(1,1),(3,3),(2,2),(4,4),(0,0)] # changes: make it a dict
    >>> short(s)
    [(0,0),(1,1),(2,2),(3,3),(4,4)]
    """
    cache = []
    for item in *args:
        item += 1
    return *args

if __name__ == '__main__':
    doctest.testmod()
