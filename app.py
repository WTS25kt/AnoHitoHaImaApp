
import requests

def get_celebrity_info(celebrity_name):
    # ニュースAPIのエンドポイント
    api_url = f"https://api.example.com/news?query={celebrity_name}&apiKey=YOUR_API_KEY"
    
    # APIリクエストを送信
    response = requests.get(api_url)
    
    # レスポンスをJSON形式で取得
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        
        # 記事のタイトルとURLを表示
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}\n")
    else:
        print("情報を取得できませんでした。")

# 有名人の名前を指定して情報を取得
get_celebrity_info("Tom Hanks")
