from collections import Counter
from operator import itemgetter

with open('words.txt','r') as f:
    words = f.readlines()

# Scrub newlines
words = [w[:-1] for w in words]
N_WORDS = len(words)

# Display the top 10 most frequent letters in position i
def freqDict(i):
    return dict(Counter([w[i] for w in words]))

freq1 = freqDict(0)
freq2 = freqDict(1)
freq3 = freqDict(2)
freq4 = freqDict(3)
freq5 = freqDict(4)

wordScores = {}
for w in words:
    wordScores[w] = freq1[w[0]] + freq2[w[1]] + freq3[w[2]] + freq4[w[3]] + freq5[w[4]]

wordScores = sorted(wordScores.items(),key=itemgetter(1),reverse=True)

print('Top 10 best starting words:')
print(wordScores[:10])
