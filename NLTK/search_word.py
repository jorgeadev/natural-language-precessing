import nltk

file = open('../NLTK.txt', "r")
read_file = file.read()
text = nltk.Text(nltk.word_tokenize(read_file))

match = text.concordance('language')