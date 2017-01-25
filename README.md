# dictify
A file to play with inspect / dis modules to show it's possible to construct a dictionnary from variables mapping variable names to their values.

    >>> x = 1
    >>> y = {"a": 2}
    >>> z = "b"
    
    >>> print(dictify(x, y, 1, z, w=3))
    {1: 1, 'x': 1, 'y': {'a': 2}, 'w': 3, 'z': 'b'}
