import os
from dotenv import load_dotenv

load_dotenv()


class FinancialSignalGenerator:
    def __init__(self):
        self.api_key = os.getenv("FMP_API_KEY")
        self.base_url = "https://financialmodelingprep.com/api/v3"
        self.symbol = "AAPL"

    def generate_signals(self):
        pass


if __name__ == "__main__":
    generator = FinancialSignalGenerator()
    generator.run()
