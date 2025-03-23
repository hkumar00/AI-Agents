from .baseclass import BaseAgent
import yfinance as yf
import ta


class TechnicalAnalysisAgent(BaseAgent):
    def __init__(self, llm_provider, max_retries=3, debug=False):
        super().__init__("TechnicalAnalysisAgent", llm_provider, max_retries, debug)

    def get_technicals(self, stock, period="12mo", interval="1d"):
        stock_data = stock.history(period=period, interval=interval)
        stock_data.dropna(inplace=True)

        technical_indicators = [
            "SMA50",
            "SMA200",
            "EMA9",
            "EMA21",
            "RSI",
            "MACD",
            "MACD_Signal",
            "Bollinger_High",
            "Bollinger_Low",
            "ATR",
            "OBV",
            "VWAP"
        ]

        # Moving Averages
        stock_data["SMA50"] = ta.trend.sma_indicator(stock_data["Close"], window=50)
        stock_data["SMA200"] = ta.trend.sma_indicator(stock_data["Close"], window=200)
        stock_data["EMA9"] = ta.trend.ema_indicator(stock_data["Close"], window=9)
        stock_data["EMA21"] = ta.trend.ema_indicator(stock_data["Close"], window=21)

        # Momentum Indicators
        stock_data["RSI"] = ta.momentum.rsi(stock_data["Close"], window=14)
        stock_data["MACD"] = ta.trend.macd(stock_data["Close"])
        stock_data["MACD_Signal"] = ta.trend.macd_signal(stock_data["Close"])

        # Volatility Indicators
        stock_data["Bollinger_High"] = ta.volatility.bollinger_hband(stock_data["Close"], window=20)
        stock_data["Bollinger_Low"] = ta.volatility.bollinger_lband(stock_data["Close"], window=20)
        stock_data["ATR"] = ta.volatility.average_true_range(stock_data["High"], stock_data["Low"], stock_data["Close"], window=14)

        # Volume Indicators
        stock_data["OBV"] = ta.volume.on_balance_volume(stock_data["Close"], stock_data["Volume"])
        stock_data["VWAP"] = ta.volume.volume_weighted_average_price(stock_data["High"], stock_data["Low"], stock_data["Close"], stock_data["Volume"])

        return stock_data.iloc[-1][technical_indicators].to_dict()

    def run(self, ticker):
        stock = yf.Ticker(ticker)
        technicals = self.get_technicals(stock, period="1y", interval="1d")

        messages = [
            {"role": "system", "content": "You are an AI assistant that specializes in technical analysis."},
            {"role": "user", "content": f"Please provide me the technical analysis of {ticker} stock based on following data:"
                                        f"\n\n{technicals}Technical Analysis:\n\n"
            }
        ]
        response = self.callLLM(messages)
        return response