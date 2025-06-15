import requests
import pandas as pd
import io   # ioモジュールをインポートします。

# 東京都のスポーツ施設一覧のcsvファイルのURL
CSV_URL = CSV_URL = "http://www.opendata.metro.tokyo.jp/2018appcon/olympic/130001sports_facilities.csv"

# データを取得する
response = requests.get(CSV_URL)

# CSVをpandasのDataFrameを利用して変換する。
sports = pd.read_csv(io.StringIO(response.content.decode("shift_jis")))

# 江東区の施設を抽出
koto_sports = sports[sports["住所"].str.contains("江東区", na=False)]

#結果を表示
for index, row in koto_sports.iterrows():
    print(f"施設名称：{row['施設名称']} / 施設分類：{row['施設分類']} / 住所：{row['住所']}")

# 参照したオープンデータは東京都オープンデータカタログサイトです。
# 概要は、東京23区及び都庁関連の様々なデータを扱っています。

# エンドポイントは"http://www.opendata.metro.tokyo.jp/2018appcon/olympic/130001sports_facilities.csv"です。

# 機能は、江東区にあるスポーツ施設を表示しています。