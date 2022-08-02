from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

d2 = [["I love this sandwich", "pos"],
      ["This is an amazing place", "pos"],
      ["I feel very good about these beers", "pos"],
      ["This is my best work", "pos"],
      ["What an awesome view", "pos"],
      ["I do not like this restaurant", "neg"],
      ["I am tired of this stuff", "neg"],
      ["I can't deal with this", "neg"],
      ["He is my sworn enemy", "neg"],
      ["My boss is horrible", "neg"],
      ["This is an awesome place", "pos"],
      ["I do not like the taste of this juice", "neg"],
      ["I love to dance", "pos"],
      ["I am sick and tired of this place", "neg"],
      ["What a great holiday", "pos"],
      ["That is a bad locality to stay", "neg"],
      ["We will have good fun tomorrow", "pos"],
      ["I went to my enemy's house today", "neg"]]

data = pd.DataFrame(d2, columns=['message', 'label'])
data['res'] = data.label.map({'pos': 1, 'neg': 0})

X = data['message']
y = data['res']

X_train, X_test, y_train, y_test = train_test_split(X, y)

cv = CountVectorizer()

X_tr = cv.fit_transform(X_train)
x_tr = cv.transform(X_test)
df = pd.DataFrame(X_tr.toarray(), columns=cv.get_feature_names_out())

nb = MultinomialNB().fit(X_tr, y_train)
predict = nb.predict(x_tr)

print('Accuracy : ', metrics.accuracy_score(y_test, predict) * 100,
      '\nConfusion Matrix :\n', metrics.confusion_matrix(y_test, predict),
      '\nPrecision Score :', metrics.precision_score(y_test, predict),
      '\nRecall Score :', metrics.recall_score(y_test, predict))
