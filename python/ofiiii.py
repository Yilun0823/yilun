{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "url = \"https://www.ofiii.com/channel/watch/4gtv-4gtv040\"\n",
    "headers = {\n",
    "    \"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36\"\n",
    "}\n",
    "\n",
    "# 發送 GET 請求並取得網頁內容\n",
    "response = requests.get(url, headers=headers)\n",
    "\n",
    "# 檢查網頁回應是否成功\n",
    "if response.status_code == 200:\n",
    "    # 取得網頁內容\n",
    "    page_content = response.text\n",
    "\n",
    "    # 在這裡進行解析網頁內容，找到.m3u8網址的位置並提取它\n",
    "    # 根據網站的實際狀況，解析方式可能不同，你可能需要使用正則表達式或解析 HTML 的庫 (如 BeautifulSoup) 來完成這個任務。\n",
    "\n",
    "    # 假設你已經得到了.m3u8的網址，存儲在變數 m3u8_url 中\n",
    "    m3u8_url = \"https://www.ofiii.com/path/to/your.m3u8\"\n",
    "    print(\"Found .m3u8 URL:\", m3u8_url)\n",
    "else:\n",
    "    print(\"Failed to retrieve the webpage. Status code:\", response.status_code)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "url = \"https://www.ofiii.com/channel/watch/4gtv-4gtv040\"\n",
    "headers = {\n",
    "    \"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36\"\n",
    "}\n",
    "\n",
    "# 發送 GET 請求並取得網頁內容\n",
    "response = requests.get(url, headers=headers)\n",
    "\n",
    "# 檢查網頁回應是否成功\n",
    "if response.status_code == 200:\n",
    "    # 取得網頁內容\n",
    "    page_content = response.text\n",
    "\n",
    "    # 使用 BeautifulSoup 解析網頁內容\n",
    "    soup = BeautifulSoup(page_content, \"html.parser\")\n",
    "\n",
    "    # 尋找包含目標 .m3u8 網址的元素\n",
    "    target_element = soup.find(\"a\", href=lambda href: href and href.endswith(\"4gtv-4gtv040-avc1_2000000=3-mp4a_143000_zho=2.m3u8\"))\n",
    "\n",
    "    if target_element:\n",
    "        m3u8_url = target_element[\"href\"]\n",
    "        print(\"Found .m3u8 URL:\", m3u8_url)\n",
    "    else:\n",
    "        print(\"The .m3u8 URL was not found on the page.\")\n",
    "else:\n",
    "    print(\"Failed to retrieve the webpage. Status code:\", response.status_code)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "\n",
    "url = \"https://www.ofiii.com/channel/watch/4gtv-4gtv040\"\n",
    "\n",
    "# 使用Selenium啟動瀏覽器並等待60秒後網頁載入完成\n",
    "driver = webdriver.Chrome()\n",
    "driver.get(url)\n",
    "wait = WebDriverWait(driver, 60)  # 等待瀏覽器最多60秒\n",
    "time.sleep(60)  # 也等待60秒，確保網頁載入完成\n",
    "\n",
    "# 使用Selenium獲取網頁內容\n",
    "page_source = driver.page_source\n",
    "\n",
    "# 關閉瀏覽器\n",
    "driver.quit()\n",
    "\n",
    "# 使用BeautifulSoup解析網頁內容\n",
    "soup = BeautifulSoup(page_source, \"html.parser\")\n",
    "\n",
    "# 定位目標視頻連結\n",
    "target_link = None\n",
    "for source_tag in soup.find_all(\"source\"):\n",
    "    src = source_tag.get(\"src\")\n",
    "    if src and \"4gtv-4gtv040-avc1_2000000=3-mp4a_143000_zho=2.m3u8\" in src:\n",
    "        target_link = src\n",
    "        break\n",
    "\n",
    "if target_link:\n",
    "    print(\"視頻連結：\", target_link)\n",
    "else:\n",
    "    print(\"未找到目標視頻連結。\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install selenium"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "The version of chrome cannot be detected. Trying with latest driver version\n"
     ]
    },
    {
     "ename": "WebDriverException",
     "evalue": "Message: unknown error: no chrome binary at path_to_your_chrome\nStacktrace:\nBacktrace:\n\tGetHandleVerifier [0x011DA813+48355]\n\t(No symbol) [0x0116C4B1]\n\t(No symbol) [0x01075358]\n\t(No symbol) [0x01091A33]\n\t(No symbol) [0x01090579]\n\t(No symbol) [0x010C0C55]\n\t(No symbol) [0x010C093C]\n\t(No symbol) [0x010BA536]\n\t(No symbol) [0x010982DC]\n\t(No symbol) [0x010993DD]\n\tGetHandleVerifier [0x0143AABD+2539405]\n\tGetHandleVerifier [0x0147A78F+2800735]\n\tGetHandleVerifier [0x0147456C+2775612]\n\tGetHandleVerifier [0x012651E0+616112]\n\t(No symbol) [0x01175F8C]\n\t(No symbol) [0x01172328]\n\t(No symbol) [0x0117240B]\n\t(No symbol) [0x01164FF7]\n\tBaseThreadInitThunk [0x75E07D59+25]\n\tRtlInitializeExceptionChain [0x77A0B79B+107]\n\tRtlClearBits [0x77A0B71F+191]\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 15\u001b[0m\n\u001b[0;32m     13\u001b[0m options\u001b[39m.\u001b[39mbinary_location \u001b[39m=\u001b[39m chrome_path  \u001b[39m# 請替換為你的Chrome瀏覽器執行檔案的路徑\u001b[39;00m\n\u001b[0;32m     14\u001b[0m options\u001b[39m.\u001b[39madd_argument(\u001b[39m\"\u001b[39m\u001b[39m--headless\u001b[39m\u001b[39m\"\u001b[39m)  \u001b[39m# 如果你想在後台運行，可以加上這個選項\u001b[39;00m\n\u001b[1;32m---> 15\u001b[0m driver \u001b[39m=\u001b[39m webdriver\u001b[39m.\u001b[39mChrome(service\u001b[39m=\u001b[39mservice, options\u001b[39m=\u001b[39moptions)\n\u001b[0;32m     17\u001b[0m \u001b[39m# 前往目標網頁\u001b[39;00m\n\u001b[0;32m     18\u001b[0m url \u001b[39m=\u001b[39m \u001b[39m\"\u001b[39m\u001b[39mhttps://www.ofiii.com/channel/watch/4gtv-4gtv040\u001b[39m\u001b[39m\"\u001b[39m\n",
      "File \u001b[1;32mc:\\Users\\a7959\\anaconda3\\Lib\\site-packages\\selenium\\webdriver\\chrome\\webdriver.py:49\u001b[0m, in \u001b[0;36mWebDriver.__init__\u001b[1;34m(self, options, service, keep_alive)\u001b[0m\n\u001b[0;32m     45\u001b[0m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mkeep_alive \u001b[39m=\u001b[39m keep_alive\n\u001b[0;32m     47\u001b[0m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mservice\u001b[39m.\u001b[39mpath \u001b[39m=\u001b[39m DriverFinder\u001b[39m.\u001b[39mget_path(\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mservice, \u001b[39mself\u001b[39m\u001b[39m.\u001b[39moptions)\n\u001b[1;32m---> 49\u001b[0m \u001b[39msuper\u001b[39m()\u001b[39m.\u001b[39m\u001b[39m__init__\u001b[39m(\n\u001b[0;32m     50\u001b[0m     DesiredCapabilities\u001b[39m.\u001b[39mCHROME[\u001b[39m\"\u001b[39m\u001b[39mbrowserName\u001b[39m\u001b[39m\"\u001b[39m],\n\u001b[0;32m     51\u001b[0m     \u001b[39m\"\u001b[39m\u001b[39mgoog\u001b[39m\u001b[39m\"\u001b[39m,\n\u001b[0;32m     52\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39moptions,\n\u001b[0;32m     53\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mservice,\n\u001b[0;32m     54\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mkeep_alive,\n\u001b[0;32m     55\u001b[0m )\n",
      "File \u001b[1;32mc:\\Users\\a7959\\anaconda3\\Lib\\site-packages\\selenium\\webdriver\\chromium\\webdriver.py:54\u001b[0m, in \u001b[0;36mChromiumDriver.__init__\u001b[1;34m(self, browser_name, vendor_prefix, options, service, keep_alive)\u001b[0m\n\u001b[0;32m     51\u001b[0m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mservice\u001b[39m.\u001b[39mstart()\n\u001b[0;32m     53\u001b[0m \u001b[39mtry\u001b[39;00m:\n\u001b[1;32m---> 54\u001b[0m     \u001b[39msuper\u001b[39m()\u001b[39m.\u001b[39m\u001b[39m__init__\u001b[39m(\n\u001b[0;32m     55\u001b[0m         command_executor\u001b[39m=\u001b[39mChromiumRemoteConnection(\n\u001b[0;32m     56\u001b[0m             remote_server_addr\u001b[39m=\u001b[39m\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mservice\u001b[39m.\u001b[39mservice_url,\n\u001b[0;32m     57\u001b[0m             browser_name\u001b[39m=\u001b[39mbrowser_name,\n\u001b[0;32m     58\u001b[0m             vendor_prefix\u001b[39m=\u001b[39mvendor_prefix,\n\u001b[0;32m     59\u001b[0m             keep_alive\u001b[39m=\u001b[39mkeep_alive,\n\u001b[0;32m     60\u001b[0m             ignore_proxy\u001b[39m=\u001b[39m\u001b[39mself\u001b[39m\u001b[39m.\u001b[39moptions\u001b[39m.\u001b[39m_ignore_local_proxy,\n\u001b[0;32m     61\u001b[0m         ),\n\u001b[0;32m     62\u001b[0m         options\u001b[39m=\u001b[39m\u001b[39mself\u001b[39m\u001b[39m.\u001b[39moptions,\n\u001b[0;32m     63\u001b[0m     )\n\u001b[0;32m     64\u001b[0m \u001b[39mexcept\u001b[39;00m \u001b[39mException\u001b[39;00m:\n\u001b[0;32m     65\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mquit()\n",
      "File \u001b[1;32mc:\\Users\\a7959\\anaconda3\\Lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:206\u001b[0m, in \u001b[0;36mWebDriver.__init__\u001b[1;34m(self, command_executor, keep_alive, file_detector, options)\u001b[0m\n\u001b[0;32m    204\u001b[0m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_authenticator_id \u001b[39m=\u001b[39m \u001b[39mNone\u001b[39;00m\n\u001b[0;32m    205\u001b[0m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstart_client()\n\u001b[1;32m--> 206\u001b[0m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstart_session(capabilities)\n",
      "File \u001b[1;32mc:\\Users\\a7959\\anaconda3\\Lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:291\u001b[0m, in \u001b[0;36mWebDriver.start_session\u001b[1;34m(self, capabilities)\u001b[0m\n\u001b[0;32m    283\u001b[0m \u001b[39m\u001b[39m\u001b[39m\"\"\"Creates a new session with the desired capabilities.\u001b[39;00m\n\u001b[0;32m    284\u001b[0m \n\u001b[0;32m    285\u001b[0m \u001b[39m:Args:\u001b[39;00m\n\u001b[0;32m    286\u001b[0m \u001b[39m - capabilities - a capabilities dict to start the session with.\u001b[39;00m\n\u001b[0;32m    287\u001b[0m \u001b[39m - browser_profile - A selenium.webdriver.firefox.firefox_profile.FirefoxProfile object. Only used if Firefox is requested.\u001b[39;00m\n\u001b[0;32m    288\u001b[0m \u001b[39m\"\"\"\u001b[39;00m\n\u001b[0;32m    290\u001b[0m caps \u001b[39m=\u001b[39m _create_caps(capabilities)\n\u001b[1;32m--> 291\u001b[0m response \u001b[39m=\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mexecute(Command\u001b[39m.\u001b[39mNEW_SESSION, caps)[\u001b[39m\"\u001b[39m\u001b[39mvalue\u001b[39m\u001b[39m\"\u001b[39m]\n\u001b[0;32m    292\u001b[0m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39msession_id \u001b[39m=\u001b[39m response\u001b[39m.\u001b[39mget(\u001b[39m\"\u001b[39m\u001b[39msessionId\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[0;32m    293\u001b[0m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mcaps \u001b[39m=\u001b[39m response\u001b[39m.\u001b[39mget(\u001b[39m\"\u001b[39m\u001b[39mcapabilities\u001b[39m\u001b[39m\"\u001b[39m)\n",
      "File \u001b[1;32mc:\\Users\\a7959\\anaconda3\\Lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:346\u001b[0m, in \u001b[0;36mWebDriver.execute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    344\u001b[0m response \u001b[39m=\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mcommand_executor\u001b[39m.\u001b[39mexecute(driver_command, params)\n\u001b[0;32m    345\u001b[0m \u001b[39mif\u001b[39;00m response:\n\u001b[1;32m--> 346\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39merror_handler\u001b[39m.\u001b[39mcheck_response(response)\n\u001b[0;32m    347\u001b[0m     response[\u001b[39m\"\u001b[39m\u001b[39mvalue\u001b[39m\u001b[39m\"\u001b[39m] \u001b[39m=\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_unwrap_value(response\u001b[39m.\u001b[39mget(\u001b[39m\"\u001b[39m\u001b[39mvalue\u001b[39m\u001b[39m\"\u001b[39m, \u001b[39mNone\u001b[39;00m))\n\u001b[0;32m    348\u001b[0m     \u001b[39mreturn\u001b[39;00m response\n",
      "File \u001b[1;32mc:\\Users\\a7959\\anaconda3\\Lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py:245\u001b[0m, in \u001b[0;36mErrorHandler.check_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    243\u001b[0m         alert_text \u001b[39m=\u001b[39m value[\u001b[39m\"\u001b[39m\u001b[39malert\u001b[39m\u001b[39m\"\u001b[39m]\u001b[39m.\u001b[39mget(\u001b[39m\"\u001b[39m\u001b[39mtext\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[0;32m    244\u001b[0m     \u001b[39mraise\u001b[39;00m exception_class(message, screen, stacktrace, alert_text)  \u001b[39m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[39;00m\n\u001b[1;32m--> 245\u001b[0m \u001b[39mraise\u001b[39;00m exception_class(message, screen, stacktrace)\n",
      "\u001b[1;31mWebDriverException\u001b[0m: Message: unknown error: no chrome binary at path_to_your_chrome\nStacktrace:\nBacktrace:\n\tGetHandleVerifier [0x011DA813+48355]\n\t(No symbol) [0x0116C4B1]\n\t(No symbol) [0x01075358]\n\t(No symbol) [0x01091A33]\n\t(No symbol) [0x01090579]\n\t(No symbol) [0x010C0C55]\n\t(No symbol) [0x010C093C]\n\t(No symbol) [0x010BA536]\n\t(No symbol) [0x010982DC]\n\t(No symbol) [0x010993DD]\n\tGetHandleVerifier [0x0143AABD+2539405]\n\tGetHandleVerifier [0x0147A78F+2800735]\n\tGetHandleVerifier [0x0147456C+2775612]\n\tGetHandleVerifier [0x012651E0+616112]\n\t(No symbol) [0x01175F8C]\n\t(No symbol) [0x01172328]\n\t(No symbol) [0x0117240B]\n\t(No symbol) [0x01164FF7]\n\tBaseThreadInitThunk [0x75E07D59+25]\n\tRtlInitializeExceptionChain [0x77A0B79B+107]\n\tRtlClearBits [0x77A0B71F+191]\n"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.service import Service as ChromeService\n",
    "from selenium.webdriver.chrome.options import Options as ChromeOptions\n",
    "import time\n",
    "\n",
    "# 設定Chrome瀏覽器的路徑和驅動程式的路徑\n",
    "chrome_path = \"path_to_your_chrome\"\n",
    "chrome_driver_path = \"path_to_your_chromedriver\"\n",
    "\n",
    "# 開啟Chrome瀏覽器\n",
    "service = ChromeService(executable_path=chrome_driver_path)\n",
    "options = ChromeOptions()\n",
    "options.binary_location = chrome_path  # 請替換為你的Chrome瀏覽器執行檔案的路徑\n",
    "options.add_argument(\"--headless\")  # 如果你想在後台運行，可以加上這個選項\n",
    "driver = webdriver.Chrome(service=service, options=options)\n",
    "\n",
    "# 前往目標網頁\n",
    "url = \"https://www.ofiii.com/channel/watch/4gtv-4gtv040\"\n",
    "driver.get(url)\n",
    "\n",
    "# 等待網頁加載完全，根據需要調整等待時間\n",
    "time.sleep(10)\n",
    "\n",
    "# 獲取Network面板的資料\n",
    "network_tab_data = driver.execute_script(\"return window.performance.getEntries();\")\n",
    "print(network_tab_data)\n",
    "\n",
    "# 關閉瀏覽器\n",
    "driver.quit()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "中視, https://ocean.ofiii.com/hls/v1/playlist/3QyaHl55EOo/master.m3u8\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "url = \"https://api.ofiii.com/cdi/v3/rpc\"\n",
    "data = {\n",
    "    \"jsonrpc\": \"2.0\",\n",
    "    \"id\": 123,\n",
    "    \"method\": \"LoadService.GetURLs\",\n",
    "    \"params\": {\n",
    "        \"media_type\": \"channel\",\n",
    "        \"device_type\": \"pc\",\n",
    "        \"asset_id\": \"4gtv-4gtv040\"\n",
    "    }\n",
    "}\n",
    "\n",
    "response = requests.post(url, json=data)\n",
    "\n",
    "if response.status_code == 200:\n",
    "    # 请求成功，处理响应数据\n",
    "    data = response.json()\n",
    "    asset_urls = data.get(\"result\", {}).get(\"asset_urls\", [])  # 从字典中获取\"asset_urls\"键的值，如果键不存在则返回空列表\n",
    "\n",
    "    if asset_urls:\n",
    "        m3u8_url = asset_urls[0]  # 取第一个.m3u8网址\n",
    "        print(\"中視,\",m3u8_url)\n",
    "    else:\n",
    "        print(\"未找到.m3u8网址\")\n",
    "else:\n",
    "    # 请求失败，处理错误信息\n",
    "    print(\"请求失败，状态码：\", response.status_code)\n",
    "    print(\"错误信息：\", response.text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://ocean.ofiii.com/hls/v1/playlist/8cpI-i0KNLA/4gtv-4gtv040-avc1_6000000=1-mp4a_143000_zho=2.m3u8\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "url = \"https://api.ofiii.com/cdi/v3/rpc\"\n",
    "data = {\n",
    "    \"jsonrpc\": \"2.0\",\n",
    "    \"id\": 123,\n",
    "    \"method\": \"LoadService.GetURLs\",\n",
    "    \"params\": {\n",
    "        \"media_type\": \"channel\",\n",
    "        \"device_type\": \"pc\",\n",
    "        \"asset_id\": \"4gtv-4gtv040\"\n",
    "    }\n",
    "}\n",
    "\n",
    "response = requests.post(url, json=data)\n",
    "\n",
    "if response.status_code == 200:\n",
    "    # 请求成功，处理响应数据\n",
    "    data = response.json()\n",
    "    asset_urls = data.get(\"result\", {}).get(\"asset_urls\", [])  # 从字典中获取\"asset_urls\"键的值，如果键不存在则返回空列表\n",
    "\n",
    "    if asset_urls:\n",
    "        m3u8_url = asset_urls[0]  # 取第一个.m3u8网址\n",
    "        modified_m3u8_url = m3u8_url.replace(\"master.m3u8\", \"4gtv-4gtv040-avc1_6000000=1-mp4a_143000_zho=2.m3u8\")\n",
    "        print( modified_m3u8_url)\n",
    "    else:\n",
    "        print(\"未找到.m3u8网址\")\n",
    "else:\n",
    "    # 请求失败，处理错误信息\n",
    "    print(\"请求失败，状态码：\", response.status_code)\n",
    "    print(\"错误信息：\", response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://ocean.ofiii.com/hls/v1/playlist/BG4M-ECPyjo/master.m3u8\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "def modify_specific_line(file_path, line_number, new_content):\n",
    "    with open(file_path, 'r') as file:\n",
    "        lines = file.readlines()\n",
    "\n",
    "    if 1 <= line_number <= len(lines):\n",
    "        lines[line_number - 1] = new_content + '\\n'\n",
    "\n",
    "    with open(file_path, 'w') as file:\n",
    "        file.writelines(lines)\n",
    "\n",
    "url = \"https://api.ofiii.com/cdi/v3/rpc\"\n",
    "data = {\n",
    "    \"jsonrpc\": \"2.0\",\n",
    "    \"id\": 123,\n",
    "    \"method\": \"LoadService.GetURLs\",\n",
    "    \"params\": {\n",
    "        \"media_type\": \"channel\",\n",
    "        \"device_type\": \"pc\",\n",
    "        \"asset_id\": \"4gtv-4gtv040\"\n",
    "    }\n",
    "}\n",
    "\n",
    "response = requests.post(url, json=data)\n",
    "\n",
    "if response.status_code == 200:\n",
    "    # 请求成功，处理响应数据\n",
    "    data = response.json()\n",
    "    asset_urls = data.get(\"result\", {}).get(\"asset_urls\", [])  # 从字典中获取\"asset_urls\"键的值，如果键不存在则返回空列表\n",
    "\n",
    "    if asset_urls:\n",
    "        m3u8_url = asset_urls[0]  # 取第一个.m3u8网址\n",
    "        new_content = f\"{m3u8_url}\"\n",
    "        print(new_content)\n",
    "\n",
    "        file_path = \"C:\\\\直播源.m3u\"\n",
    "        line_number_to_modify = 3  # 修改第三行\n",
    "        modify_specific_line(file_path, line_number_to_modify, new_content)\n",
    "    else:\n",
    "        print(\"未找到.m3u8网址\")\n",
    "else:\n",
    "    # 请求失败，处理错误信息\n",
    "    print(\"请求失败，状态码：\", response.status_code)\n",
    "    print(\"错误信息：\", response.text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "#EXTM3U\n",
      "#EXTINF:-1,中視\n",
      "https://ocean.ofiii.com/hls/v1/playlist/25jtzbyz8Ek/master.m3u8\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "def 修改檔案(file_path, new_content):\n",
    "    with open(file_path, 'w') as file:\n",
    "        file.write(new_content)\n",
    "\n",
    "url = \"https://api.ofiii.com/cdi/v3/rpc\"\n",
    "data = {\n",
    "    \"jsonrpc\": \"2.0\",\n",
    "    \"id\": 123,\n",
    "    \"method\": \"LoadService.GetURLs\",\n",
    "    \"params\": {\n",
    "        \"media_type\": \"channel\",\n",
    "        \"device_type\": \"pc\",\n",
    "        \"asset_id\": \"4gtv-4gtv040\"\n",
    "    }\n",
    "}\n",
    "\n",
    "response = requests.post(url, json=data)\n",
    "\n",
    "if response.status_code == 200:\n",
    "    # 請求成功，處理回應資料\n",
    "    data = response.json()\n",
    "    asset_urls = data.get(\"result\", {}).get(\"asset_urls\", [])  # 從字典中取得\"asset_urls\"鍵的值，如果鍵不存在則返回空列表\n",
    "\n",
    "    if asset_urls:\n",
    "        m3u8_url = asset_urls[0]  # 取第一個.m3u8網址\n",
    "        new_content = f\"#EXTM3U\\n#EXTINF:-1,中視\\n{m3u8_url}\"\n",
    "        print(new_content)\n",
    "\n",
    "        file_path = \"C:\\\\直播源.m3u\"\n",
    "        修改檔案(file_path, new_content)\n",
    "    else:\n",
    "        print(\"未找到.m3u8網址\")\n",
    "else:\n",
    "    # 請求失敗，處理錯誤資訊\n",
    "    print(\"請求失敗，狀態碼：\", response.status_code)\n",
    "    print(\"錯誤資訊：\", response.text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "#EXTINF:-1,台視\n",
      "https://ocean.ofiii.com/hls/v1/playlist/n_wsVSPgqc0/master.m3u8\n",
      "#EXTINF:-1,中視\n",
      "https://ocean.ofiii.com/hls/v1/playlist/nKYMXgu3jFU/master.m3u8\n",
      "#EXTINF:-1,華視\n",
      "https://ocean.ofiii.com/hls/v1/playlist/3Ycp2A0J6FM/master.m3u8\n",
      "#EXTINF:-1,好消息1台\n",
      "https://ocean.ofiii.com/hls/v1/playlist/8zSJhfDpHOw/master.m3u8\n",
      "#EXTINF:-1,好消息2台\n",
      "https://ocean.ofiii.com/hls/v1/playlist/G8sMgU8HyzM/master.m3u8\n",
      "#EXTINF:-1,ELTV生活英語台\n",
      "https://ocean.ofiii.com/hls/v1/playlist/4qykqJf2wvw/master.m3u8\n",
      "#EXTINF:-1,龍華卡通台\n",
      "https://ocean.ofiii.com/hls/v1/playlist/_JMXS9HmdR4/master.m3u8\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Popen: returncode: None args: ['C:\\\\Program Files\\\\DAUM\\\\PotPlayer\\\\PotPlay...>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "import subprocess\n",
    "\n",
    "def 清除檔案內容(file_path):\n",
    "    with open(file_path, 'w') as file:\n",
    "        file.truncate(0)\n",
    "\n",
    "def 修改檔案(file_path, new_content):\n",
    "    with open(file_path, 'a') as file:\n",
    "        file.write(new_content + '\\n')\n",
    "\n",
    "channel_ids = [\"4gtv-4gtv066\",\"4gtv-4gtv040\", \"4gtv-4gtv041\",\"litv-ftv16\",\"litv-ftv17\",\"litv-longturn20\",\"litv-longturn01\"]  # 要請求的頻道ID列表\n",
    "\n",
    "url = \"https://api.ofiii.com/cdi/v3/rpc\"\n",
    "\n",
    "# 清除檔案內容\n",
    "file_path = \"C:\\\\直播源.m3u\"\n",
    "清除檔案內容(file_path)\n",
    "\n",
    "# 添加第一行 \"#EXTM3U\"\n",
    "修改檔案(file_path, \"#EXTM3U\")\n",
    "\n",
    "for channel_id in channel_ids:\n",
    "    data = {\n",
    "        \"jsonrpc\": \"2.0\",\n",
    "        \"id\": 123,\n",
    "        \"method\": \"LoadService.GetURLs\",\n",
    "        \"params\": {\n",
    "            \"media_type\": \"channel\",\n",
    "            \"device_type\": \"pc\",\n",
    "            \"asset_id\": channel_id\n",
    "        }\n",
    "    }\n",
    "\n",
    "    response = requests.post(url, json=data)\n",
    "\n",
    "    if response.status_code == 200:\n",
    "        # 請求成功，處理回應資料\n",
    "        data = response.json()\n",
    "        asset_urls = data.get(\"result\", {}).get(\"asset_urls\", [])  # 從字典中取得\"asset_urls\"鍵的值，如果鍵不存在則返回空列表\n",
    "\n",
    "        if asset_urls:\n",
    "            m3u8_url = asset_urls[0]  # 取第一個.m3u8網址\n",
    "            if channel_id == \"4gtv-4gtv066\":\n",
    "                channel_name = \"台視\"\n",
    "            elif channel_id == \"4gtv-4gtv040\":\n",
    "                channel_name = \"中視\"\n",
    "            elif channel_id == \"4gtv-4gtv041\":\n",
    "                channel_name = \"華視\"\n",
    "            elif channel_id == \"litv-ftv16\":\n",
    "                channel_name = \"好消息1台\"\n",
    "            elif channel_id == \"litv-ftv17\":\n",
    "                channel_name = \"好消息2台\"\n",
    "            elif channel_id == \"litv-longturn20\":\n",
    "                channel_name = \"ELTV生活英語台\"\n",
    "            elif channel_id == \"litv-longturn01\":\n",
    "                channel_name = \"龍華卡通台\"\n",
    "            else:\n",
    "                channel_name = \"未知頻道\"\n",
    "\n",
    "            new_content = f\"#EXTINF:-1,{channel_name}\\n{m3u8_url}\"\n",
    "            print(new_content)\n",
    "\n",
    "            修改檔案(file_path, new_content)\n",
    "        else:\n",
    "            print(f\"未找到 {channel_id} 的.m3u8網址\")\n",
    "    else:\n",
    "        # 請求失敗，處理錯誤資訊\n",
    "        print(f\"請求 {channel_id} 失敗，狀態碼：\", response.status_code)\n",
    "        print(\"錯誤資訊：\", response.text)\n",
    "\n",
    "# 使用subprocess打開檔案\n",
    "potplayer_exe = \"C:\\\\Program Files\\\\DAUM\\\\PotPlayer\\\\PotPlayerMini64.exe\"\n",
    "subprocess.Popen([potplayer_exe, file_path])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File saved: C:\\Users\\a7959\\Desktop\\channels.m3u\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import requests\n",
    "\n",
    "def save_m3u_file(content, file_path):\n",
    "    with open(file_path, \"w\") as f:\n",
    "        f.write(content)\n",
    "\n",
    "channel_ids = [\n",
    "    \"4gtv-4gtv066\", \"4gtv-4gtv040\", \"4gtv-4gtv041\",\n",
    "    \"litv-ftv16\", \"litv-ftv17\", \"litv-longturn20\", \"litv-longturn01\"\n",
    "]\n",
    "\n",
    "url = \"https://api.ofiii.com/cdi/v3/rpc\"\n",
    "\n",
    "all_content = \"\"\n",
    "\n",
    "for channel_id in channel_ids:\n",
    "    data = {\n",
    "        \"jsonrpc\": \"2.0\",\n",
    "        \"id\": 123,\n",
    "        \"method\": \"LoadService.GetURLs\",\n",
    "        \"params\": {\n",
    "            \"media_type\": \"channel\",\n",
    "            \"device_type\": \"pc\",\n",
    "            \"asset_id\": channel_id\n",
    "        }\n",
    "    }\n",
    "\n",
    "    response = requests.post(url, json=data)\n",
    "\n",
    "    if response.status_code == 200:\n",
    "        # 请求成功，处理响应数据\n",
    "        data = response.json()\n",
    "        asset_urls = data.get(\"result\", {}).get(\"asset_urls\", [])\n",
    "\n",
    "        if asset_urls:\n",
    "            m3u8_url = asset_urls[0]  # 取第一個.m3u8網址\n",
    "            if channel_id == \"4gtv-4gtv066\":\n",
    "                channel_name = \"台視\"\n",
    "            elif channel_id == \"4gtv-4gtv040\":\n",
    "                channel_name = \"中視\"\n",
    "            elif channel_id == \"4gtv-4gtv041\":\n",
    "                channel_name = \"華視\"\n",
    "            elif channel_id == \"litv-ftv16\":\n",
    "                channel_name = \"好消息1台\"\n",
    "            elif channel_id == \"litv-ftv17\":\n",
    "                channel_name = \"好消息2台\"\n",
    "            elif channel_id == \"litv-longturn20\":\n",
    "                channel_name = \"ELTV生活英語台\"\n",
    "            elif channel_id == \"litv-longturn01\":\n",
    "                channel_name = \"龍華卡通台\"\n",
    "            else:\n",
    "                channel_name = \"未知頻道\"\n",
    "\n",
    "            new_content = f\"#EXTINF:-1,{channel_name}\\n{m3u8_url}\\n\"\n",
    "            all_content += new_content\n",
    "        else:\n",
    "            print(f\"未找到 {channel_id} 的.m3u8網址\")\n",
    "    else:\n",
    "        # 請求失敗，處理錯誤資訊\n",
    "        print(f\"請求 {channel_id} 失敗，狀態碼：\", response.status_code)\n",
    "        print(\"錯誤資訊：\", response.text)\n",
    "\n",
    "# Save the content to a .m3u file on the desktop\n",
    "desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')\n",
    "file_path = os.path.join(desktop_path, \"channels.m3u\")\n",
    "save_m3u_file(all_content, file_path)\n",
    "print(\"File saved:\", file_path)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
