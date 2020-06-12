from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "In this tutorial, I\'m learning NLTK. It is an interesting platform."
stop_words = set(stopwords.words('english'))
words = word_tokenize(text)

new_sentence = []

for word in words:
    if word not in stop_words:
        new_sentence.append(word)


print(new_sentence)