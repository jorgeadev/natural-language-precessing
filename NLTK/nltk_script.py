import nltk
from nltk.corpus import stopwords

print(nltk.__version__)

#nltk.download()
nltk.download('stopwords')

print(set(stopwords.words('English')))
print(set(stopwords.words('Spanish')))
print(set(stopwords.words('Italian')))
print(set(stopwords.words('French')))