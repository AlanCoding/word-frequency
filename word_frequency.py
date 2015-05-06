import re
import sys

def clean_text(text):
    """Sanitizes text by replacing all non-alpha chars with spaces"""
    cleaned = text.lower()
    cleaned = re.sub(r'[^a-z]'," ",cleaned)
    return cleaned

def word_frequency(text):
    """Dictionary of words by frequency of occurrence in text"""
    word_counts = {}
    for word in clean_text(text).split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            if allow_word(word):
                word_counts[word] = 1
    return word_counts

def top_20_words(word_counts):
    """List of top 20 words by frequency given count dictionary"""
    return sorted(word_counts, key=word_counts.get, reverse=True)

def count_print(list,word_counts):
    """Prints words in list and occurrences in dictionary"""
    for i in range(20):
        print(list[i].ljust(12)+str(word_counts[list[i]]))

def bar_graph(list,word_counts):
    """Prints ASCII bar graph of normalized frequency of words"""
    ratio = 50./word_counts[list[0]]
    for i in range(20):
        print(list[i].ljust(12)+"#"*int(ratio*word_counts[list[i]]))

def allow_word(word):
    """Boolean that makes a decision to include word or not"""
    exclude_list = ["a","able","about","across","after","all","almost","also","am","among","an","and","any","are","as","at","be"
    ,"because","been","but","by","can","cannot","could","dear","did","do","does","either","else","ever","every"
    ,"for","from","get","got","had","has","have","he","her","hers","him","his","how","however","i","if","in","into","is"
    ,"it","its","just","least","let","like","likely","may","me","might","most","must","my","neither","no","nor"
    ,"not","of","off","often","on","only","or","other","our","own","rather","said","say","says","she","should"
    ,"since","so","some","than","that","the","their","them","then","there","these","they","this","tis","to","too"
    ,"twas","us","wants","was","we","were","what","when","where","which","while","who","whom","why","will","with"
    ,"would","yet","you","your"]
    if word in exclude_list:
        return False
    else:
        return True

"""Main program, only executes when argument is present"""
if len(sys.argv)>1:
    filename = sys.argv[1]
    with open(filename) as file:
        word_counts = word_frequency(file.read())
    top20 = top_20_words(word_counts)
    count_print(top20,word_counts)
    bar_graph(top20,word_counts)
