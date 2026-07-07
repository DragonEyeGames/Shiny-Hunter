import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1524026707235962901/V18xvnObNPSTyu_hTA42l9OedNI2goqL354bgfgocbFCAQ-2EKNswEzBrKA9ntNFIDSM"

def send_discord_update(message):
    payload = {"content": message}
    response = requests.post(WEBHOOK_URL, json=payload)
    
    if response.status_code == 204:
        print("Update sent successfully!")
    else:
        print(f"Failed to send update: {response.status_code}")

def send_rich_embed(title, description, color=3447003):
    payload = {
        "embeds": [{
            "title": title,
            "description": description,
            "color": color
        }]
    }
    requests.post(WEBHOOK_URL, json=payload)

send_discord_update("Restarting Hunt")