import random

def analyze_forex_signal(symbol, timeframe):
    # Dummy logic – replace with real RSI + MACD + EMA logic
    rsi = random.uniform(30, 70)
    macd = 0.0
    ema21 = random.uniform(1.0, 2.0)

    trend = "up" if rsi > 50 else "down"

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "RSI": round(rsi, 2),
        "MACD": macd,
        "EMA21": round(ema21, 4),
        "trend": trend
    }
