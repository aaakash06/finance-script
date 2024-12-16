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
        endpoint = f"{self.BASE_URL}/{statement_type}/{self.symbol}?limit=2&apikey={self.API_KEY}"
        
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {statement_type}: {e}")
            return []

if __name__ == "__main__":
    generator = FinancialSignalGenerator()
    generator.run()
