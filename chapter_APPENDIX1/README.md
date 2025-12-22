# 日本語感情分析モデル＆Azure AI Language連携ツール

## 概要
日本語テキストの感情分析を行うための学習・推論スクリプトと、Azure AI Languageサービスを利用した感情分析スクリプトが含まれます。自作モデルとクラウドAIの両方で感情分析を実行・比較できます。

## 環境構築
- visual studio code
- GitHub Copilot（CSV生成用プロンプトを使用するため）
- python 3.8以上
- pip
- Azure AI Languageのエンドポイントとキー（Azureアカウントが必要）

## 作業ディレクトリへの移動
以下の作業を実施する前に、ターミナルから以下のコマンドを実行してワーキングディレクトリを変更してください。
```
cd chapter_APPENDIX1
```

## インストール手順
1. 必要なパッケージをインストール
```
pip install -r requirements/requirements.txt
```
Azure AI Languageを利用する場合は、さらに以下を実行
```
pip install -r requirements/requirements_azure.txt
```

2. `.env.example` をコピーして `.env` を作成し、Azureのエンドポイントとキーを記入

## 使用方法
### 1. 学習用データの準備とモデル学習
- `sentiment_data.csv`（日本語テキストとラベルのCSV）を用意してください。  
  
> [!NOTE]
> GitHub CopilotでCSVを用意する場合、以下のプロンプトをGitHub Copilotに入力して、必要なファイルを生成してください。
>```
>日本語の感情分析モデルの学習用に使うsentiment_data.csvを生成し、以下の条件でCSV形式のサンプルデータを50件分出力してください。
>- フィールドは2つ：「text」（日本語の文章）,「label」（0~2の数字で表した感情ラベル）
>- 感情ラベルは「ポジティブ」、「ニュートラル」、「ネガティブ」の3種類とし、できるだけ均等に分布させてください
>- 文章はSNSの投稿やレビューのような短めの文（20〜50文字程度）で自然な内容にしてください。
>```

- モデルトレーニング:  
以下のコマンドで、感情分析モデルをトレーニングします。
```
python train_sentiment_model.py
```

### 2. 自作モデルで感情分析
以下のコマンドで、トレーニング済みモデルを使用して感情分析を行います。
```
python predict_sentiment.py
```

### 3. Azure AI Languageで感情分析
Azure AI Languageサービスで取得したエンドポイントとキーを`.env`ファイルに設定してください。  
`.env`ファイルの例は`.env.example`を参照してください。  
>[!NOTE]
> Azure AI Languageを利用する場合、事前にAzureポータルでAI Languageサービスを作成し、エンドポイントとキーを取得する必要があります。

以下のコマンドで、Azure AI Languageを使った感情分析を実行できます。
```
python predict_sentiment_azure.py
```

## 依存関係
- requirements/requirements.txt: pandas, scikit-learn, janome, joblib
- requirements/requirements_azure.txt: python-dotenv, requests

## 注意
- `.gitignore`により、モデルデータ・CSV・.envファイルはGitで追跡されません。
  （`.env.example`はサンプルとして追跡されます。）