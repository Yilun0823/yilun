import requests

url = "https://m.litv.tv/api/urls"
data = {
    "AssetId": "4gtv-4gtv040",
    "MediaType": "channel",
    "puid": "aa1593a5-71e6-4820-a830-72f18e5206ec"
}

# 添加 Cookie 到請求中 (請根據你的 Cookie 資訊填寫)
cookies = {
    "PUID": "1bc32f7d-94b6-4570-8f38-31e08dafe055",
    "_gcl_au": "1.1.184968446.1689974529",
    "_gid": "GA1.2.1454316267.1689974529",
    "_ga_73WWD84D3P": "GS1.1.1689984923.2.1.1689985877.32.0.0",
    "l_de": "4A494942E127",
    "__uid_2": "%7B%22refresh_from%22%3A1689988583446%2C%22refresh_expires%22%3A1692576983446%2C%22identity_expires%22%3A1690071383446%2C%22advertising_token%22%3A%22AgAAA26KyLlckuXirlwE14gcGhAa5pxOKHY5UJ7RfLbmF5oJejcZBg%2B%2FiqpW5Ud5BAfuq%2FYTOwYT2dTrgzSkDcDrB3CUmgYKVqV5wq7i3U6QDr20R9rU3ZsNOyil%2FlZL2vbkEPLRtwjQAX9D%2FE%2Bqzet7s17cj060redxdH4TzCcBxWHJew%3D%3D%22%2C%22refresh_token%22%3A%22AAAAA29O3UFoI2plc458Us8I2Fx0BAXSmNzfcRCad1vlzwRhMxw5OVy5ci14%2BJ%2F%2B81ofjJEeL8LfF8KDDUE%2B%2B5xCTdYl3OG9KVRqbWGC24YXQvjnL9QpNwGBlAkf36P6euO9kyFFLemBWdwk9qHTu8UlrOyPfxt4EUAQigV6BGohqot2mat8k8UTTA3cPMR8f1G%2BGpO97IDQvbuU0b%2Bouo3dm1S50Chdo4LonRpUYkq1YbfhZmiMST3paGaZU6WZI3bJEJLCYg6axhEOoD5kJLU1EfE3jmWVMXitEOa0DCqNQPlcXbNKuFeInavWSVbzeXcKbpNRXDLL33vTYNff67rjzwmC7Vwd2j59TdHTAJ6nJ8zH1DGOf88zJX2VG1PWcA1Y%22%2C%22refresh_response_key%22%3A%22kRtdfMyL0Qq03IPyrf9p2PoMcmSBMEMQFrugBrA3OcI%3D%22%7D",
    "_gat_gtag_UA_59507085_6": "1",
    "l_us": "tjiDF8%2Fm8K5oLOO3EUqzAQ%3D%3D",
    "l_pa": "iFNyK3Zfdu4gg65X%2BbLFzw%3D%3D",
    "l_ac": "WIw73QNQMXyL5M75zEFX8eXO%2BcMAq6ce3nz%2BhWHlqRE%3D",
    "l_to": "6NyVLXJAMLO4kDYdFwMRJ%2BaAt9Ydgno5LSLSrd762w1j2wbhZZVzTg%2F7UC%2BlhpC5",
    "_ga": "GA1.2.2048553477.1689974529",
    "_gat_gtag_UA_59507085_1": "1",
    "_gat_gtag_UA_145078221_1": "1",
    "_ga_73WWD84D3P": "GS1.1.1689984923.2.1.1689985877.32.0.0",
    "_ga_F72R6P7EZK": "GS1.1.1689984958.2.1.1689985883.55.0.0"
}

response = requests.post(url, json=data, cookies=cookies)

if response.status_code == 200:
    try:
        # 請求成功，處理回應資料
        result = response.json().get("result")
        if result is not None:
            asset_urls = result.get("AssetURLs", [])
            if len(asset_urls) > 0:
                m3u8_url_with_params = asset_urls[0]
                # 使用 split() 函數分割字串，只取得 .m3u8 檔案本身的網址
                m3u8_url = m3u8_url_with_params.split("?")[0]
                # 印出 .m3u8 檔案的網址
                print("中視,", m3u8_url)

                # 將 .m3u8 檔案的網址寫入 litv.txt 檔案中
                with open("litv.txt", "w") as file:
                    file.write(f"中視, {m3u8_url}")
            else:
                print("沒有找到 .m3u8 檔案的網址")
        else:
            print("回應資料中沒有 'result' 鍵")
    except ValueError as e:
        print("回應資料解析錯誤:", e)
else:
    # 請求失敗，處理錯誤訊息
    print("請求失敗，狀態碼：", response.status_code)
    print("錯誤訊息：", response.text)
