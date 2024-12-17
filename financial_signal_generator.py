import os
from dotenv import load_dotenv
import requests
from typing import List, Dict

load_dotenv()


class FinancialSignalGenerator:
    def __init__(self):
        self.API_KEY = os.getenv("FMP_API_KEY")
        self.BASE_URL = "https://financialmodelingprep.com/api/v3"
        self.symbol = "AAPL"

    def fetch_financial_data(self, statement_type: str) -> List[Dict]:
        """Fetch financial statements from FMP API"""
        endpoint = f"{self.BASE_URL}/{statement_type}/{self.symbol}?period=annual&limit=2&apikey={self.API_KEY}"
        
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {statement_type}: {e}")
            return []



    def generate_signal(self, metric: str, current: float, previous: float, 
                       statement_type: str) -> Dict:
        """Generate a SIGNAL dictionary for a metric"""
        sentiment, rating = self.calculate_trend(current, previous)
        
        return {
            "summary": f"AAPL {metric} {'increased' if current > previous else 'decreased'} "
                      f"from {previous:,.2f} to {current:,.2f} in the last year.",
            "symbol": self.symbol,
            "topics": [statement_type, metric],
            "sentiment": sentiment,
            "rating": rating,
            "timeframe": "1Y"
        }


if __name__ == "__main__":
    generator = FinancialSignalGenerator()
    generator.run()
