import numpy as np
import random
import re
from collections import defaultdict

songListPath = 'content/mountainGoatsSongList.txt'
with open (songListPath) as f:
    text = f.read()
tokenized_text = [
    word
    for word in re.split('\W+', text)
    if word != ''
]
#print (tokenized_text)

markov_graph = defaultdict(lambda: defaultdict(int))

last_word = tokenized_text[0].lower()
for word in tokenized_text[1:]:
    word = word.lower()
    markov_graph[last_word][word] += 1
    last_word = word

nonEndWords = ['and', 'the', 'to', 'is', 'for', 'going']
nonStartWords = ['s']

def getRandomWord(wordDict, wordType = ''):
    # Word types can be Start or End of left blank
    # Certain words will not start or end a title
    while True:
        randomWord = random.choice(list(wordDict.keys()))

        if wordType == 'Start':
            if randomWord not in nonStartWords:
                return randomWord
        elif wordType == 'End':
            if randomWord not in nonEndWords:
                return randomWord
        else:
            return randomWord

#random first word
#first_word = random.choice(tokenized_text)
def walk_graph(graph, distance = 6, start_node=None):
    #Returns a list of words from a randomly weighted walk

    # will not end in any word in words in the nonEndWords list
    if distance <= 0 and start_node not in nonEndWords:
        return []
    # If not given, pick start node at random
    if not start_node:
        start_node = getRandomWord(graph, 'start')

    # evenly weights each choice
    weights = np.array(
        list(markov_graph[start_node].values()),
        dtype=np.float64)
    weights /= weights.sum()

    # pick a destination using weighted distribution
    choices = list(markov_graph[start_node].keys())
    chosen_word = np.random.choice(choices, None, p=weights)

    return [chosen_word] + walk_graph(
        graph, distance=distance-1,
        start_node=chosen_word)


for i in range(10):
    n = random.randint(2, 5)
    print(' '.join(walk_graph(
        markov_graph, distance=n)), '\n')
