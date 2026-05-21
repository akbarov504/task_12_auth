from flask import Flask, jsonify
from token_manager import get_valid_token, get_token_info

app = Flask(__name__)

@app.get("/token")
def token():
    token = get_valid_token()
    info = get_token_info()
    return jsonify({
        "token": token,
        "truck_id": info.get("truck_id"),
        "expires_at": info.get("expires_at"),
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8787)
