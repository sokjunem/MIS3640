#Exercise_1
def sumall(*args):
    '''returns sum of all the arguments
    '''
    result = 0
    for number in args:
        result += number
    return result

print(sumall(1, 2, 3, 4, 5, 6, 7))

#Exercise_2
def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.
    s: string
    Returns: list of letters
    """
    hist = make_histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res


def make_histogram(s):
    """Make a map from letters to number of times they appear in s.
    s: string
    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename, encoding="utf8").read()


string = read_file('trump_at_RNC.txt')
letter_seq = most_frequent(string)
for x in letter_seq:
    print(x)