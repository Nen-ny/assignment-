# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as openfile:
        read_file = openfile.read()

        return read_file
print(read_file_content("./story.txt"))


def count_words():
    """
    Counts the occurrence of words in a text
    :param text: string
    :return: dictionary
    """

    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = text.split()
    word_count = {}
    for i in words:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] =1
    return word_count
print(count_words())
