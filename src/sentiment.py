from textblob import TextBlob
import pandas as pd

def analyze_sentiment(csv_path):
    df = pd.read_csv(csv_path)
    df['Sentiment'] = df['Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    df.to_csv(csv_path.replace('.csv', '_sentiment.csv'), index=False)
    return df