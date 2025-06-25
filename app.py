from flask import Flask
import threading, time
import sub4sub_campaign

app = Flask(__name__)

@app.route("/")
def ping():
    return "🟢 I am alive"

# Start background loop
def background_loop():
    while True:
        sub4sub_campaign.run_campaigns_for_all_tokens()
        print("🕒 Sleeping for 6 hours...\n")
        time.sleep(6 * 60 * 60)

threading.Thread(target=background_loop, daemon=True).start()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
