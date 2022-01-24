
def punctuation(text):
  punct = '''"\.?@#$%^&*_~='',!()-[]{\}\;:<>"'''

  for chars in text:
    if chars in punct:
      text = text.replace(chars, '')
  return text

def histogram(text_inputed):
  # Open text file, read the file and enter into the 'file' variable  
  file = open(text_inputed, 'r')
  # Open text, input into the 'file' variable 
  text = file.read()
  file.close()

  text = text.lower()

  text_without_punctuation = punctuation(text)

  word_list = text_without_punctuation.split()
  histogram = {}


  for word in word_list:
      if word not in histogram:
          histogram[word] = 1
      else: 
          histogram[word] += 1

  return histogram

def unique_words(histogram):
  return len(histogram)

def frequency(word, histogram):
  return histogram[word.lower()]

if __name__ == '__main__':
    histogram_test = histogram('testsampletext.txt')
    print(histogram_test)
    words_test = unique_words(histogram_test)
    print(words_test)
    count_test = frequency('fish', histogram_test)
    print(count_test)