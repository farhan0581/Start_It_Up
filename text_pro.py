from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import csv
import numpy as np
from numpy import array

handle=open('sample_dish.csv','rt')
reader=csv.DictReader(handle)

train_set=[]
response_t=[]

for line in reader:
	train_set.append(line['dish'])
	if line['type']=='non-veg':
		response_t.append(1)
	else:
		response_t.append(0)

response_t=array(response_t)
print response_t.shape


# train_set = ("The sky is blue.", "The sun is bright.")
# test_set = ("The sun in the sky is bright.",
# "We can see the shining sun, the bright sun.")




count_vectorizer = CountVectorizer(stop_words='english')
tr=count_vectorizer.fit_transform(train_set)


tfidf_transformer = TfidfTransformer()
tr_tfidf = tfidf_transformer.fit_transform(tr)


clf = MultinomialNB().fit(tr_tfidf, response_t)


docs_new = ['fish rice', 'fish karahi paneer','fish fry','chily chicken','dal punjabi']

X_new_counts = count_vectorizer.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

# for doc, category in zip(docs_new, predicted):
	# print('%r => %s' % (doc, twenty_train.target_names[category]))


print predicted

# print "Vocabulary:", count_vectorizer.vocabulary_

# count_vectorizer.get_feature.names()

# freq_term_matrix = count_vectorizer.transform(train_set)

# print freq_term_matrix.todense()