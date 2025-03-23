from .baseclass import BaseAgent
import yfinance as yf


class FundamentalAnalysisAgent(BaseAgent):
    def __init__(self, llm_provider, max_retries=3, debug=False):
        super().__init__("FundamentalAnalysisAgent", llm_provider, max_retries, debug)

    def get_financials(self, stock):
        info = stock.info
        financials = {
            "marketCap": info.get("marketCap", "N/A"),
            "P/E Ratio": info.get("trailingPE", "N/A"),
            "forwardPE": info.get("forwardPE", "N/A"),
            "PEG Ratio": info.get("pegRatio", "N/A"),
            "Price/Sales": info.get("priceToSalesTrailing12Months", "N/A"),
            "Price/Book": info.get("priceToBook", "N/A"),
            "EPS Growth": info.get("earningsGrowth", "N/A"),
            "Revenue Growth": info.get("revenueGrowth", "N/A"),
            "ROA": info.get("returnOnAssets", "N/A"),
            "ROE": info.get("returnOnEquity", "N/A"),
            "Debt/Equity Ratio": info.get("debtToEquity", "N/A"),
            "Current Ratio": info.get("currentRatio", "N/A"),
            "Dividend Yield": info.get("dividendYield", "N/A"),
            "EV/EBITDA": info.get("enterpriseToEbitda", "N/A"),
            "ROCE": info.get("returnOnCapitalEmployed", "N/A"),
            "Operating margin": info.get("operatingMargins", "N/A"),
            "freeCashFlow": info.get("freeCashflow", "N/A"),
        }
        return financials

    def run(self, ticker):
        stock = yf.Ticker(ticker)
        financials = self.get_financials(stock)

        messages = [
            {"role": "system", "content": "You are an AI assistant that specializes in fundamental analysis."},
            {"role": "user", "content": f"Please provide me the fundamental analysis of {ticker} stock based on following data: {financials}.\n\nFundamental Analysis:\n\n"},
        ]
        response = self.callLLM(messages)
        return response