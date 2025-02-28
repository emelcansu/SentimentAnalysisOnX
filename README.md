# Twitter ile Duygu Analizi ve Vibe Coding Yaklaşımı

Bu proje, Twitter API'sini kullanarak `#yazılım` hashtag'li tweet'leri toplar, NLTK'nin VADER modülü ile duygu analizi yapar ve sonuçları görselleştirir. Ayrıca, geliştirme sürecinde **"vibe coding"** yaklaşımının nasıl uygulandığını gösterir.

## Özellikler
- **Twitter API Entegrasyonu:** Twitter API v2 kullanılarak gerçek zamanlı tweet'ler çekilir.
- **Duygu Analizi:** NLTK'nin VADER modülü kullanılarak tweet'lerin duygu skorları (pozitif, negatif, nötr) hesaplanır.
- **Veri Görselleştirme:** Seaborn ve Matplotlib kullanılarak duygu dağılımı görselleştirilir.
- **Vibe Coding Yaklaşımı:** Yazılım geliştirme sürecinde "vibe coding" yaklaşımının nasıl uygulanabileceği gösterilir.

## Nasıl Çalışır?
1. **Tweet Toplama:** Twitter API'sine bağlanılarak `#yazılım` hashtag'li tweet'ler çekilir.
2. **Duygu Analizi:** Her bir tweet, NLTK'nin VADER modülü kullanılarak analiz edilir ve duygu skoru hesaplanır.
3. **Veri Görselleştirme:** Duygu dağılımı, bir grafik üzerinde görselleştirilir.
4. **CSV Olarak Kaydetme:** Analiz sonuçları, ileri analizler için bir CSV dosyasına kaydedilir.

## Neden "Vibe Coding"?
Bu proje, yazılım geliştirme sürecinde **"vibe coding"** yaklaşımını kullanarak, yaratıcılığı, esnekliği ve kişisel motivasyonu ön plana çıkarır. Bu yaklaşım, geliştiricilerin akışta kalmasını, fikirlerini denemesini ve kod yazma sürecinden keyif almasını teşvik eder.

## Gereksinimler
- Python 3.x
- Kütüphaneler: `tweepy`, `pandas`, `nltk`, `matplotlib`, `seaborn`, `python-dotenv`
- Twitter API Bearer Token

## Nasıl Çalıştırılır?
1. Depoyu klonlayın.
2. Gerekli kütüphaneleri `pip install -r requirements.txt` komutu ile yükleyin.
3. Twitter API Bearer Token'ınızı `.env` dosyasına ekleyin.
4. `python code.py` komutu ile script'i çalıştırın.

## Çıktılar
![image](https://github.com/user-attachments/assets/f0789219-fd77-4496-a977-9ad39a49940c)
