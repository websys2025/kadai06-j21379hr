import requests

APP_ID = "fb847d81dc7c57f3d84c7dc468867bd44dad8b85"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0003268145", # 学校基本調査
    "cdArea":"13000", # 東京都
    "cdCat01": "E2101", # 小学校数（校）
    "metaGetFlg":"N",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)


# エンドポイントは"https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"になります。
# 機能は学校基本調査から東京都の小学校数を表示しました。