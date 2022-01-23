

def histogram(choosen_text):
  f = open(choosen_text, 'r')
  text = f.read()
  f.close()
  text = text.lower()
  punct = '''"\.?@#$%^&*_~='',!()-[]{\}\;:<>"'''

  for chars in text:
    if chars in punct:
      text = text.replace(chars, '')

  split_words = text.split()
  print(split_words)

  histogram = []

  for words in split_words:
    found = False
    for tuple in histogram:
      if tuple[0] == words:
        number = tuple[1]
        number += 1
        histogram.remove(tuple)
        histogram.append((words, number))
        found = True
        break
    if found is False:
      histogram.append((words, 1))

  return histogram


def unique_words(histogram):
  return len(histogram)

def frequency(histogram, word):
  for tuple in histogram:
    if tuple[0] == word.lower():
      return tuple[1]

if __name__ == '__main__':
  print_historgram = histogram("testsampletext.txt")
  print(print_historgram)
  length_historgram = unique_words(print_historgram)
  print(length_historgram)
  word_historgram = frequency(print_historgram, 'FisH')
  print(word_historgram)