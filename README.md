
#  Discord Bot for Ngrok with Python & SSH tunnel


## 主要功能：

 - Discord 是容易使用的通訊軟體，亦可以建立機器人提供服務。
 - 本程式利用Python結合Ngrok API 作為外出時可以利用 [termux](https://termux.com/) 連線回家。  [SSH是什麼？](https://ithelp.ithome.com.tw/articles/10277498)

---

## 套件需求：
 * pyngrok
 *  discord.py
 * requests

```
python -m pip install -r requirement.txt
```
### 運作環境：Python 3.6+

---


## 實際功能：

```
請求日期：2022-06-26            這是收到使用者請求的時間
請求時間：20:07:24
系統已運作：10 days, 4:05:02    這是上機時間
內部IP：192.168.1.102           這是路由器 LAN 的 IP
外部IP：118.---.---.179         這是外部的 IP (如果有開啟 Port Forwarding 封包轉送)
可使用的ngrok地址：
4.tcp.ngrok.io:1--60"           如果沒有 Port Forwarding，此地址轉送到網際網路供外部存取
```
## 程式碼設定：
```
# Ngrok 設定 請到 Ngrok Dashboard 複製 token
ngrok.set_auth_token("<ngrok-token>")

# TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
client.run('<Discord-bot-token>')  
```

---
## 進階使用：

`SSH Port 是 22`

`FTP Port 是 21`

`如果有需求，
改成 Minecraft Sever Port 亦可以在不干涉路由器設定，
讓外部朋友連線遊玩`

 ## 請注意， ~~不是麥塊玩家福音~~

---

## 預覽：
![Alt text](Assets/demo.jpg?raw=true "Title")

---


## 警告：
 <h1> Ngrok 是外部服務，資訊安全問題請三思後再使用 </h1>

## 參見：
 - [建立Discord 機器人](https://hackmd.io/@kangjw/Discordpy%E6%A9%9F%E5%99%A8%E4%BA%BA%E5%BE%9E0%E5%88%B01%E8%B6%85%E8%A9%B3%E7%B4%B0%E6%95%99%E5%AD%B8)


 - [取得IP](https://shengyu7697.github.io/python-get-ip/)
 - [SSH是什麼？](https://ithelp.ithome.com.tw/articles/10277498)
 - [termux 官方文件](https://termux.com/)

  Ngrok API ：如何使用 PyNgrok
 
 * [PyNgrok 官方文件](https://pyngrok.readthedocs.io/en/latest/index.html)
 * [介紹 Ngrok 功能](https://ithelp.ithome.com.tw/articles/10197345) 
