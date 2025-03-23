import ollama
from .baseclass import BaseAgent

class DecisionAgent(BaseAgent):
    def __init__(self, llm_provider, max_retries=3, debug=False):
        super().__init__("DecisionAgent", llm_provider, max_retries, debug)

    def run(self, ticker, fundamental_analysis, technical_analysis):
        self.fundamental_analysis = fundamental_analysis
        self.technical_analysis = technical_analysis
        self.ticker = ticker

        prompt = f"""
        Analyze the stock {self.ticker} based on the following fundamental and technical analysis:

        Fundamental Analysis:
        {self.fundamental_analysis}

        Technical Analysis:
        {self.technical_analysis}

        Think about the anaysis provided and what the stock's future prospects might be.
        Based on your analysis, should I buy, sell, or hold this stock? Provide reasoning.
        """

        messages = [
            {"role": "system", "content": "You are an AI assistant that specializes in taking stock buy/sell/hold decisions, based on your deep understanding of fundamental and technical analysis."},
            {"role": "user", "content": prompt}
        ]
        response = self.callLLM(messages)
        return response
