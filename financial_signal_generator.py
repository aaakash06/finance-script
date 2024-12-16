import os
from dotenv import load_dotenv

load_dotenv()


class FinancialSignalGenerator:
    def __init__(self):
        self.api_key = os.getenv("FMP_API_KEY")

    def generate_signals(self):
        pass

