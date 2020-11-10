class Hamming:

    """
    >>> hamming = Hamming()
    >>> hamming.distance('','')
    0
    >>> hamming.distance('A', '')
    Traceback (most recent call last):
    ...
    ValueError: strings should be the same length
    >>> hamming.distance('', 'A')
    Traceback (most recent call last):
    ...
    ValueError: strings should be the same length
    >>> hamming.distance('A','A')
    0
    >>> hamming.distance('X','D')
    1
    >>> hamming.distance('ABCDEF', 'GHIJKL')
    6
    >>> hamming.distance('a', 'A')
    1
    >>> hamming.distance('ABCD', 'ABGH')
    2
    >>> hamming.distance('XDJAREKMAKOTA','XDALAMAKOTA')
    Traceback (most recent call last):
    ...
    ValueError: strings should be the same length
    >>> hamming.distance(21,  3)
    Traceback (most recent call last):
    ...
    ValueError: params should be strings
    """

    def distance(self, string1, string2):
        if type(string1) == str and type(string2) == str:
            if len(string1) == len(string2):
                if string1 == string2:
                    return 0
                else:
                    counter = 0
                    for i in range(0, len(string1)):
                        if string1[i] != string2[i]:
                            counter += 1
                    return counter
            else:
                raise ValueError("strings should be the same length")
        else:
            raise ValueError("params should be strings")

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
