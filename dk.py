from telethon.sync import TelegramClient

# Your credentials (keep them private)
api_id = 29277030
api_hash = "07885b2e5a680e98c287f1ebf8ff2a0e"

# Create client session
client = TelegramClient("terabox_session", api_id, api_hash)

async def main():
    me = await client.get_me()
    print("Logged in as:", me.username)

    # Example: get info about a channel or group
    entity = await client.get_entity("https://t.me/telegram")
    print("Channel title:", entity.title)

with client:
    client.loop.run_until_complete(main())
