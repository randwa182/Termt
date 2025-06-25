import threading
import time
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "✅ I'm alive!", 200

url = "https://sub.tubeforces.com/api/campaign/v3/campaigns/"
boundary = "92a0a36c-06a9-416d-bc26-a5c6a3fdaeda"

tokens = [
    "Sub4Sub 192219dbb53da290fb361a6064a522cc6fef8f2c",
    "Sub4Sub d443681681bb7475a2cf504906ea23f67cf2adc1",
    "Sub4Sub c9ee031d85e08469fa4c974e7fe3dcdb5477fe7a"
]

def build_multipart_data():
    fields = {
        "type": "view",
        "subscribes": "0",
        "views": "10",
        "likes": "0",
        "comments": "0",
        "view_duration": "45",
        "cost": "900",
        "reward": "67",
        "currency": "1",
        "video.uid": "ArW6tIr5bE4",
        "video.title": "🔥 Ultimate NCS Music Mix 2025 | Best No Copyright Songs | EDM, Trap, Dubstep 🎧",
        "video.thumbnail_url": "https://i.ytimg.com/vi/ArW6tIr5bE4/mqdefault.jpg",
        "channel.uid": "UCwVJdHJb1h-q3apf3PduBcw",
        "channel.title": "Kheti Tanks",
        "channel.thumbnail_url": "https://yt3.ggpht.com/h9-rhbJbBcrW17Z7FVlO6D8YG5KPjulof0Z3rOLln8zGHt8bGKtq5B377i47iQh9IdhStQDmDg=s88-c-k-c0x00ffffff-no-rj",
        "channel.description": ""
    }

    body = ""
    for key, value in fields.items():
        body += f"--{boundary}\r\n"
        body += f'Content-Disposition: form-data; name="{key}"\r\n\r\n{value}\r\n'
    body += f"--{boundary}--\r\n"
    return body.encode("utf-8")

def background_worker():
    while True:
        for token in tokens:
            headers = {
                "App-Locale": "en",
                "Authorization": token,
                "Package-Name": "com.tubeforces.get_sub",
                "Apk-Version": "129",
                "Time-Zone": "Asia_Kolkata",
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "User-Agent": "okhttp/3.14.9",
                "Accept-Encoding": "gzip",
                "Connection": "Keep-Alive",
                "Host": "sub.tubeforces.com"
            }

            print(f"📡 Sending POST request with token: {token[-6:]}")
            try:
                r = requests.post(url, headers=headers, data=build_multipart_data())
                if r.status_code == 201:
                    print(f"✅ Success ID: {r.json().get('id')}")
                else:
                    print(f"❌ Error {r.status_code}: {r.text}")
            except Exception as e:
                print(f"❌ Exception: {e}")
        print("⏳ Sleeping for 6 hours...\n")
        time.sleep(6 * 60 * 60)

threading.Thread(target=background_worker, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)