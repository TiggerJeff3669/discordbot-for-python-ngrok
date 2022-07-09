
# 時間正規化
from datetime import datetime, timedelta

# 執行內網穿透Ngrok
from pyngrok import ngrok

# 導入 Discord.py
import discord

# 查詢IP
from requests import get
import socket
import re

# 格式化查詢時間
import psutil
import time

# client 是我們與 Discord 連結的橋樑
client = discord.Client()

# Ngrok 設定
ngrok.set_auth_token("<ngrok-token>")
ngip = ngrok.connect(22, "tcp")  # SSH通道、為了從外部IP連線回主機
ngip = re.search('tcp://(.*?)->', str(ngip)).group(1)
print("Ngrok 已啟動")


# 調用 event 函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)


@client.event
# 當有訊息時
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    # 如果包含 ip，機器人回傳 SSH/Ngrok資料
    if message.content == 'ip':
        await message.delete()
        # 加載外部IP external IP Address 業者IP
        extip = get('https://api.ipify.org').text
        # 加載內部IP inner IP Address (Router Address)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        # 日期格式
        date = datetime.now().strftime('%Y-%m-%d')
        times = datetime.now().strftime('%H:%M:%S')
        # 在線時長
        uptime = time.time() - psutil.boot_time()
        uptime = str(timedelta(seconds=round(uptime)))
        # print(s.getsockname()[0])
        s.close()
        package = (
            '```yaml\n請求日期：{}\n請求時間：{}\n系統已運作：{}\n內部IP：{}\n外部IP：{}\n可使用的ngrok地址：\n{}\n```'
            .format(date, times, uptime, ip, extip, ngip))
        await message.channel.send(package)


client.run('<Discord-bot-token>')  # TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
