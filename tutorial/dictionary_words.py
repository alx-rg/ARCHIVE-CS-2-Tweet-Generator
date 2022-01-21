import random
import sys

numbers = int(sys.argv[1])
# Open and read the word file
dictionary = open('./words-sample.txt', 'r')

word_lines = dictionary.read().splitlines()
length_of_dict = len(word_lines)

# close the word file
dictionary.close()

#New array for words
random_selection = []

index = 0
while index < numbers:
  new_word = word_lines[random.randint(0,length_of_dict)]
  random_selection.append(new_word)
  index += 1

# print(len(word_lines))
new_random_sentence = ' '.join(random_selection)
print(random_selection)