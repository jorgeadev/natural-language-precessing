#from textacy.datasets import Wikipedia
from nltk.corpus import wikipedia
# Descargando copus de wikipedia
wp = Wikipedia(data_dir='../WIKI', lang='es', version='latest')
wp.download()

