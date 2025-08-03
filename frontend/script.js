async function getSignal() {
  const symbol = document.getElementById("symbol").value;
  const response = await fetch(`https://your-backend-url/api/signal?symbol=${symbol}&timeframe=1m`);
  const data = await response.json();

  document.getElementById("result").innerHTML = `
    <p><strong>Symbol:</strong> ${data.symbol}</p>
    <p><strong>Timeframe:</strong> ${data.timeframe}</p>
    <p><strong>RSI:</strong> ${data.RSI}</p>
    <p><strong>MACD:</strong> ${data.MACD}</p>
    <p><strong>EMA21:</strong> ${data.EMA21}</p>
    <p><strong>Trend:</strong> <span style="color: ${data.trend === 'up' ? 'green' : 'red'}">${data.trend.toUpperCase()}</span></p>
  `;
}
