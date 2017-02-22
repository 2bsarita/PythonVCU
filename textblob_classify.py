# Please install textblob module

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ("My boss is horrible.", "neg"),
    ('I feel very good about these beers.', 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg')

    ]

cl = NaiveBayesClassifier(train)

print(cl.classify("I feel great!"))
blob = TextBlob("hangover is horrible, but the beer is good", classifier=cl)

for s in blob.sentences:
     print(s)
     print(s.classify())
