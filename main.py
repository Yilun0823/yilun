import json
import requests

def get_m3u8_url(channel_id):
    url = "https://m.litv.tv/api/urls"
    data = {
        "AssetId": channel_id,
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
        # 請求成功，處理回應資料
        try:
            result = response.json().get("result", {})
            asset_urls = result.get("AssetURLs", [])
            if len(asset_urls) > 0:
                m3u8_url_with_params = asset_urls[0]
                # 使用 split() 函數分割字串，只取得 .m3u8 檔案本身的網址
                m3u8_url = m3u8_url_with_params.split("?")[0]
                return m3u8_url
            else:
                return None
        except Exception as e:
            print("解析回應資料時發生錯誤：", e)
            return None
    else:
        # 請求失敗，處理錯誤訊息
        print("請求失敗，狀態碼：", response.status_code)
        print("錯誤訊息：", response.text)
        return None

def remove_lines_after(file_path, line_number):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if line_number < 0 or line_number >= len(lines):
        return

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines[:line_number+1])

# 從 channels.json 讀取頻道資料
with open("channels.json", 'r', encoding='utf-8') as f:
    channels = json.loads(f.read())

# 變數來存儲 tv.txt 和 tv.m3u 的內容
txt_content = "LITV頻道,#genre#\n"
m3u_content = "#EXTM3U\n"

for channel_data in channels:
    asset_id = channel_data["id"]
    m3u8_url = get_m3u8_url(asset_id)
    if m3u8_url:
        title = channel_data["title"]
        
        # 添加到 tv.txt 的內容
        txt_content += title + ',' + m3u8_url + '\n'
        
        # 添加到 tv.m3u 的內容
        m3u_content += f'#EXTINF:-1 tvg-logo="{title}" tvg-name="{title}" group-title="LITV頻道",{title}\n{m3u8_url}\n'
# 寫入 tv.txt
with open("tv.txt", 'w', encoding='utf-8') as f:
    f.write(txt_content)

# 寫入 tv.m3u
with open("tv.m3u", 'w', encoding='utf-8') as f:
    f.write(m3u_content)

# 先將 5433.txt 內第 732 行後的資料都刪除
remove_lines_after("5433.txt", 732)

# 讀取 tv.txt 內所有內容
with open("tv.txt", 'r', encoding='utf-8') as f:
    tv_content = f.read()

# 將 tv.txt 內容加入 5433.txt 內
with open("5433.txt", 'a', encoding='utf-8') as f:
    f.write(tv_content)
