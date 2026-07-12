import json
import cv2
import requests

NONSHINY_URL = "https://discord.com/api/webhooks/1524026707235962901/V18xvnObNPSTyu_hTA42l9OedNI2goqL354bgfgocbFCAQ-2EKNswEzBrKA9ntNFIDSM"

SHINY_URL = "https://discord.com/api/webhooks/1524064459033940131/DLA5vBhAQl_iyVv45qNBYtFugQaYBGeOVxwz1mttrYaTBj2vHndjP3lBte_7pwiycwcr"

ERROR_URL = "https://discord.com/api/webhooks/1524064922139496460/j-YTI6HA0f28obvb7IcSZz9vKA9V-Fa8rRTEDEAf0FB8OMWKn6xZEjWHZB__CCumiqf8"

def send_discord_update(message):
    payload = {"content": message}
    response = requests.post(NONSHINY_URL, json=payload)
    
    if response.status_code == 204:
        print("Update sent successfully!")
    else:
        print(f"Failed to send update: {response.status_code}")

def send_shiny_notification(title, description, frame=None, color=3447003):
    embed_data = {
        "title": title,
        "description": description,
        "color": color
    }
    
    # Check if a valid OpenCV frame was passed
    if frame is not None:
        filename = "shiny_screenshot.png"
        embed_data["image"] = {"url": f"attachment://{filename}"}

    payload = {
        "embeds": [embed_data]
    }

    if frame is not None:
        # 1. Compress the frame into PNG format in memory
        success, encoded_image = cv2.imencode('.png', frame)
        if not success:
            print("Failed to encode frame")
            return

        # 2. Convert the compressed buffer into bytes
        file_bytes = encoded_image.tobytes()
        
        # 3. Package the request as multipart/form-data
        data_payload = {"payload_json": json.dumps(payload)}
        file_payload = {"file": (filename, file_bytes, "image/png")}
        
        requests.post(SHINY_URL, data=data_payload, files=file_payload)
    else:
        # Fallback to text-only if frame reading fails
        requests.post(SHINY_URL, json=payload)

def send_failure_notification(title, description, color=3447003):
    payload = {
        "embeds": [{
            "title": title,
            "description": description,
            "color": color
        }]
    }
    requests.post(ERROR_URL, json=payload)