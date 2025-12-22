import joblib
import pandas as pd
from janome.tokenizer import Tokenizer

pipeline = joblib.load('sentiment_model.pkl')


def tokenize(text):
    t = Tokenizer()
    return ' '.join([token.surface for token in t.tokenize(text)])

label_map = {0: 'ポジティブ', 1: 'ニュートラル', 2: 'ネガティブ'}
labels = pipeline.classes_

while True:
    text = input('感情分析したい文章を入力してください（終了するにはexitと入力）：')
    if text.lower() == 'exit':
        break
    wakati = tokenize(text)
    X = [wakati]
    pred = pipeline.predict(X)[0]
    proba = pipeline.predict_proba(X)[0]
    confidence = proba[list(labels).index(pred)]
    print(f'判定: {label_map.get(pred, pred)}')
    print('信頼度: {:.1f}%'.format(confidence * 100))
    print('--- 詳細 ---')
    for label, p in zip(labels, proba):
        print(f'{label_map.get(label, label)}: {p*100:.1f}%')
