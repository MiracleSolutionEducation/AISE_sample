import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
import joblib
from janome.tokenizer import Tokenizer

def tokenize(text):
    t = Tokenizer()
    return ' '.join([token.surface for token in t.tokenize(text)])

df = pd.read_csv('sentiment_data.csv')

df['wakati'] = df['text'].apply(tokenize)

y = df['label']
X = df['wakati']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000, random_state=42))
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(pipeline, 'sentiment_model.pkl')
print('モデルをsentiment_model.pklとして保存しました')
