from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


categories=['alt.atheism', 'soc.religion.christian',
               'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train',
   									categories=categories, shuffle=True, random_state=42)

print twenty_train.get('target_names')




count_vect = CountVectorizer(stop_words='english')
X_train_counts = count_vect.fit_transform(twenty_train.data)# text

# frequency of words
# print count_vect.vocabulary_
print X_train_counts.shape

print twenty_train.target.shape
# tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
# X_train_tf = tf_transformer.transform(X_train_counts)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

print X_train_tfidf

clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)


docs_new = ['what is ?', 'OpenGL on the GPU is fast','i have a fast brain','religion creates divide','oh my jesus']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
	print('%r => %s' % (doc, twenty_train.target_names[category]))
# print twenty_train.