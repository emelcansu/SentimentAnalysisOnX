import tweepy
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Backend'i değiştiriyoruz
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os
from dotenv import load_dotenv
import time

# .env dosyasını yükle
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

client = tweepy.Client(bearer_token=BEARER_TOKEN)

query = "#yazılım -is:retweet lang:tr"
max_tweets = 1500  # Define how many tweets you want

data = []
next_token = None

try:
    while len(data) < max_tweets:
        try:
            tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["text"], next_token=next_token)

            if tweets.data:
                for tweet in tweets.data:
                    text = tweet.text
                    sentiment_score = sia.polarity_scores(text)['compound']
                    sentiment = "Pozitif" if sentiment_score > 0.05 else "Negatif" if sentiment_score < -0.05 else "Nötr"
                    data.append([text, sentiment_score, sentiment])

            # Eğer daha fazla tweet varsa, pagination yap
            next_token = tweets.meta.get("next_token") if "next_token" in tweets.meta else None
            if not next_token:
                break

        except tweepy.errors.TooManyRequests as e:
            print("Hız limiti aşıldı, bekleniyor...")
            time.sleep(15 * 60)  # 15 dakika bekle
            continue

except KeyboardInterrupt:
    print("Kullanıcı tarafından durduruldu.")
    # Kodunuzu burada düzgün şekilde sonlandırabilirsiniz

# Veri çekildiğini kontrol et
if not data:
    print("Hiç veri bulunamadı.")
else:
    print(f"Toplam {len(data)} tweet analiz edildi.")

    # Veriyi DataFrame'e dönüştür
    df = pd.DataFrame(data, columns=["Tweet", "Sentiment Score", "Sentiment"])

    # Veriyi yazdırma
    print("Veri Örneği:")
    print(df.head())  # Verilerin ilk 5 satırını yazdır

    # Grafiği oluştur
    plt.figure(figsize=(12, 8))  # Grafiği daha büyük yapalım
    sns.countplot(x="Sentiment", data=df, palette="viridis")
    plt.title("Tweet Sentiment Dağılımı")
    plt.xlabel("Duygu")
    plt.ylabel("Tweet Sayısı")
    plt.xticks(rotation=45)  # Etiketleri döndürebiliriz
    plt.tight_layout()  # Grafiğin kenar boşluklarını düzeltir
    plt.show()

    # CSV dosyasını kaydetme
    df.to_csv("tweet_sentiment_analysis.csv", index=False)
    print("Analiz tamamlandı ve CSV dosyası kaydedildi.")
