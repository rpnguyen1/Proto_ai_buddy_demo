from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # <-- this line enables CORS for all routes

PASSCODE = os.getenv("PASSCODE", "1234")

@app.route("/api/test", methods=["POST"])
def test():
    data = request.get_json()
    code = data.get("passcode", "")
    if code == PASSCODE:
        return jsonify({"ok": True, "message": "hello world"})
    else:
        return jsonify({"ok": False, "message": "wrong passcode"})

if __name__ == "__main__":
    app.run(port=5001, debug=True)

    #test
