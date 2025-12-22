import os
import requests
from dotenv import load_dotenv

load_dotenv()

AZURE_ENDPOINT = os.getenv('AZURE_LANGUAGE_ENDPOINT')
AZURE_KEY = os.getenv('AZURE_LANGUAGE_KEY')

assert AZURE_ENDPOINT, 'AZURE_LANGUAGE_ENDPOINTが設定されていません'
assert AZURE_KEY, 'AZURE_LANGUAGE_KEYが設定されていません'

headers = {
    'Ocp-Apim-Subscription-Key': AZURE_KEY,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

analyze_url = AZURE_ENDPOINT.rstrip('/') + "/language/:analyze-text?api-version=2023-04-01"

while True:
    text = input('感情分析したい文章を入力してください（終了するにはexitと入力）：')
    if text.lower() == 'exit':
        break
    data = {
        "kind": "SentimentAnalysis",
        "parameters": {
            "modelVersion": "latest"
        },
        "analysisInput": {
            "documents": [
                {"id": "1", "language": "ja", "text": text}
            ]
        }
    }
    response = requests.post(analyze_url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        doc = result['results']['documents'][0]
        sentiment = doc['sentiment']
        confidence = doc['confidenceScores']
        sentiment_map = {'positive': 'ポジティブ', 'neutral': 'ニュートラル', 'negative': 'ネガティブ'}
        print(f'判定: {sentiment_map.get(sentiment, sentiment)}')
        print(f'判定結果の信頼度: {confidence[sentiment]*100:.1f}%')
        print('--- 各ラベルの信頼度 ---')
        for k, v in confidence.items():
            print(f'{sentiment_map.get(k, k)}: {v*100:.1f}%')
    else:
        print('APIリクエストに失敗しました:', response.text)
