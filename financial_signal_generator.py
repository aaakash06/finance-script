import json
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


    def calculate_trend(self, current: float, previous: float) -> tuple:
        """Calculate trend and determine sentiment"""
        if current == previous:
            return "Hold", 5
        
        percent_change = ((current - previous) / previous) * 100
        
        if percent_change > 10:
            return "Buy", 8
        elif percent_change > 0:
            return "Buy", 6
        elif percent_change > -10:
            return "Hold", 4
        else:
            return "Sell", 2
        
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


    def process_statements(self) -> List[Dict]:
        """Process all financial statements and generate signals"""
        statements = {
            "income-statement": "Income Statement",
            "balance-sheet-statement": "Balance Sheet",
            "cash-flow-statement": "Cash Flow"
        }
        
        signals = []
        
        for endpoint, statement_type in statements.items():
            data = self.fetch_financial_data(endpoint)
            
            if len(data) < 2:
                continue
                
            current_year = data[0]
            previous_year = data[1]
            
            # Process numerical metrics
            for key in current_year.keys():
                if isinstance(current_year[key], (int, float)) and key not in ['date', 'period']:
                    try:
                        current_value = float(current_year[key])
                        previous_value = float(previous_year[key])
                        
                        signal = self.generate_signal(
                            key, 
                            current_value,
                            previous_value,
                            statement_type
                        )
                        signals.append(signal)
                    except (ValueError, TypeError):
                        continue
        
        return signals

    def run(self):
        """Main execution method"""
        signals = self.process_statements()
        
        # Save signals to JSON file
        with open('signals.json', 'w') as f:
            json.dump(signals, f, indent=2)
        
        print(f"Generated {len(signals)} signals and saved to signals.json")
        
        # Print first 3 signals as examples
        print("\nExample Signals:")
        for signal in signals[:3]:
            print(json.dumps(signal, indent=2))
        
        # Print expansion ideas
        print("\nExpansion Ideas:")
        print("1. Implement machine learning models to predict future metric trends")
        print("2. Add sentiment analysis from news and social media to enhance signals")
        print("3. Scale to analyze multiple companies and identify sector-wide trends")


if __name__ == "__main__":
    generator = FinancialSignalGenerator()
    generator.run()
