# Marc Mounzer's common_words.py for Bleacher Report
# 8/24/2018

# This method finds the common elements of the two passed arrays and returns them.  Works for more than just words :)
def common_words(first_array, second_array):
    commons = []

    for first_word in first_array:
        if first_word in second_array and first_word not in commons:
            commons.append(first_word)

    return commons

first_array = eval(input('Enter a list of words: '))
second_array = eval(input('Enter another list of words: '))
print(f'The common words are: {common_words(first_array,second_array)}')