from telethon import TelegramClient, events
import os

# מקבל מה‑Environment Variables של ריילווי
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient('session', api_id, api_hash)

# רשימת הקבוצות למעקב (שם מוסיפים בריילווי, לא כאן)
source_chats = os.getenv("SOURCE_CHATS").split(",")

# הקבוצה שלך (גם בריילווי)
target_chat = os.getenv("TARGET_CHAT")

@client.on(events.NewMessage(chats=source_chats))
async def handler(event):
    if event.message.message:  # שולח רק טקסט
        await client.send_message(target_chat, event.message.message)

client.start()
client.run_until_disconnected()
