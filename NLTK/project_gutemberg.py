import nltk

# nltk.download('gutenberg')
gutenberg_files = nltk.corpus.gutenberg.fileids()
print("\n")
print("Length = " + str(len(gutenberg_files)))

print(gutenberg_files)
print("\n")

gutenberg_list = [
    'austen-emma.txt',
    'austen-persuasion.txt',
    'austen-sense.txt',
    'bible-kjv.txt',
    'blake-poems.txt',
    'bryant-stories.txt',
    'burgess-busterbrown.txt',
    'carroll-alice.txt',
    'chesterton-ball.txt',
    'chesterton-brown.txt',
    'chesterton-thursday.txt',
    'edgeworth-parents.txt',
    'melville-moby_dick.txt',
    'milton-paradise.txt',
    'shakespeare-caesar.txt',
    'shakespeare-hamlet.txt',
    'shakespeare-macbeth.txt',
    'whitman-leaves.txt'
]

# Get number of words of "bryant-stories.txt" of Gutenberg Project.
bryant_words = nltk.corpus.gutenberg.words("bryant-stories.txt")
print("Number of words = " + str(len(bryant_words)))
