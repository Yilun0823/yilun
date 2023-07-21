<?php
// 检查请求是否携带了直播源地址参数
if (isset($_GET['url']) && !empty($_GET['url'])) {
    // 获取直播源地址
    $liveStreamUrl = $_GET['url'];

    // 设置代理头部信息，模拟浏览器访问，防止部分服务器禁止非浏览器请求
    $headers = [
        'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    ];

    // 初始化 cURL 会话
    $ch = curl_init();

    // 设置 cURL 选项
    curl_setopt($ch, CURLOPT_URL, $liveStreamUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    // 执行 cURL 会话并获取返回的数据
    $response = curl_exec($ch);

    // 获取响应的 MIME 类型
    $contentType = curl_getinfo($ch, CURLINFO_CONTENT_TYPE);

    // 关闭 cURL 会话
    curl_close($ch);

    // 设置代理响应头部信息，以便将直播源数据传递给客户端
    header("Content-Type: $contentType");

    // 输出直播源数据
    echo $response;
} else {
    // 如果没有传递直播源地址参数，返回错误信息或者重定向到其他页面
    echo "Error: Live stream URL not provided.";
}
?>
