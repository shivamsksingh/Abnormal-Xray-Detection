from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Application Name": "X-Ray Scan using ML", "Version": "1.0", "Type":"REST"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
