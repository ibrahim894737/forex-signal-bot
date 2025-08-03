from flask import Flask, request, jsonify
from indicators import analyze_forex_signal

app = Flask(__name__)

@app.route("/signal", methods=["GET"])
def get_signal():
    symbol = request.args.get("symbol", "EURUSD")
    timeframe = request.args.get("timeframe", "1m")
    signal = analyze_forex_signal(symbol, timeframe)
    return jsonify(signal)

if __name__ == "__main__":
    app.run()
