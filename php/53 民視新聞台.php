<?php
$token=$_GET['token'];
$expires=$_GET['expires'];
$token1=$_GET['token1'];
$expires1=$_GET['expires1'];

$url="https://4gtvfreepc-cds.cdn.hinet.net/live/pool/litv-ftv13/4gtv-live-mid/index.m3u8?token="$token"&expires="$expires"&token1="$token1"&expires1"$expires1";
header('location:'.urldecode($url));
?>
