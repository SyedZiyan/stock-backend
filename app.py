from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/stock")
def stock():
    return jsonify([
        {"symbol": "AAPL", "price": 267.26},
        {"symbol": "MSFT", "price": 412.10},
        {"symbol": "RELIANCE.BSE", "price": 2450.30},
        {"symbol": "TCS.BSE", "price": 3890.50},
        {"symbol": "INFY.BSE", "price": 1560.75}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)