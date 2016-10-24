import string
import nltk.corpus

def process_file(filename):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding = 'utf8')
    stop = set(stopwords.words('english'))

    for line in fp:
        
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace
        
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
        
            if word not in stop:
                #update the histogram
                hist[word] = hist.get(word, 0) + 1
            
    
    return hist

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)

def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    temp = []
    for word, frequency in hist.items():
        temp.append((frequency, word))
    
    temp.sort() # only sogrts first elements in the list
    temp.reverse()
    return temp

def main(filename):
    sentence = filename
    hist = process_file(filename)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)



main('conjuring_review_1.txt')
main('conjuring_review_2.txt')
main('conjuring_review_Combined.txt')

sentence = open('conjuring_review_7.txt', 'r')
sentence.close