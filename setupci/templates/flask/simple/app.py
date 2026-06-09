from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"message": "Hello, World! Welcome to your Flask app."})

@app.route("/items/<int:item_id>")
def read_item(item_id):
    return jsonify({"item_id": item_id, "status": "active"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
