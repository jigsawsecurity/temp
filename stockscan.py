import yfinance as yf
from your_indicator_library import calculate_indicators
from your_notification_system import send_text_message

def analyze_stock(stock_ticker):
    data = yf.download(stock_ticker)
    indicators = calculate_indicators(data)
    bullish_count = sum(1 for ind in indicators if ind == 'bullish')
    bearish_count = sum(1 for ind in indicators if ind == 'bearish')
    
    if bullish_count / len(indicators) >= 0.70:
        send_text_message(f"{stock_ticker} is mostly bullish")
    elif bearish_count / len(indicators) >= 0.70:
        send_text_message(f"{stock_ticker} is mostly bearish")

stock_tickers = ['AAPL', 'MSFT', 'GOOG', ...]  # List of stock tickers
for ticker in stock_tickers:
    analyze_stock(ticker)
