<?php
// 目標 m3u8 URL
$targetUrl = 'http://fvla1.netboxtv.top/live/fchcah3u/31t5z7bp/index.m3u8';

// 使用 cURL 初始化請求
$ch = curl_init($targetUrl);

// 設置請求頭部信息
$headers = array(
    'User-Agent: Lavf/58.12.100',
    'Accept: */*',
    'Connection: keep-alive',
    'Host: fvla1.netboxtv.top',
    'Icy-MetaData: 1',
    'userid: userid:44665',
    'usertoken: usertoken:9df3e9958efa06e7032c6ee4cf632c0f-1691067498-2011-44665-api.live.vod.dvr.static.apk'
);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

// 設置返回響應而不直接輸出
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// 執行 cURL 請求並獲取響應內容
$response = curl_exec($ch);

// 檢查請求是否成功
if (curl_getinfo($ch, CURLINFO_HTTP_CODE) === 200) {
    // 設置返回的 Content-Type 和 Content-Length 頭部信息
    header('Content-Type: application/x-mpegURL');
    header('Content-Length: ' . strlen($response));

    // 輸出響應內容
    echo $response;
} else {
    // 請求失敗，返回相應的錯誤信息
    header('HTTP/1.1 500 Internal Server Error');
    echo 'Request failed with status code: ' . curl_getinfo($ch, CURLINFO_HTTP_CODE);
}

// 關閉 cURL 會話
curl_close($ch);
?>
