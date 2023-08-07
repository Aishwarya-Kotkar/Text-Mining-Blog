from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "This is an example of stop word filteration."
stop_words =  set (stopwords.words("english")) # set of the stopwords from english language
#print(stop_words)

words = word_tokenize(example) #tokenize the sentence into words
filtered_sents = []

for w in words : 
    if w not in stop_words: # if the word is not in stopword list then append that word into filtered_sents
        filtered_sents.append(w)       
print(filtered_sents)

#filtered_sents= [w for w in words if not w in stop_words]
#print(filtered_sents) 