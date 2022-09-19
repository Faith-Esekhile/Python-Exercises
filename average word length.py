total = 0
num_words = 0

input_word = input('Please enter a word or press enter to quit: ')


while input_word != '':
    input_word = input('Please enter a word or press enter to quit: ')
    length_word = len(input_word)
    total += length_word
    num_words += 1



avg = total/(num_words-1)

print('Average length of word is:',format(avg ,'.1f'))










