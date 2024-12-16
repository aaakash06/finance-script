** Test: Extracting Financial Data and Generating SIGNALs 🚀**

---

### Task Overview

Write a **single Python script** that:

1. Fetches **income statement**, **balance sheet**, and **cash flow statement** for the **last two years** for a "AAPL" stock symbol using the Financial Modeling Prep API (https://site.financialmodelingprep.com/).
2. Processes **all available metrics** from these statements to generate SIGNALs in the specified format.
3. Expands on your approach with three innovative ideas in case of additional resources.

---

### Instructions

#### Step 1: Fetch Financial Statements

- Use the Financial Modeling Prep API to extract the **income statement**, **balance sheet**, and **cash flow statement** for the last two yeards.
- Parse the data into a structured format (e.g., a dictionary or DataFrame).
- Handle API rate limits and errors securely.

#### Step 2: Generate SIGNALs

For **each metric** in the financial statements:

1. Analyze trends between the two years (e.g., increase or decrease).
2. Generate a SIGNAL in the following format:

```python
{
    summary (str): summary under 200 words
    symbol (str): Stock symbol.
    topics (List[str]): Relevant topics (e.g., "earnings", "dividends").
    sentiment (str): Sentiment ("Buy", "Sell", "Hold").
    rating (int): Numerical rating on a 0-10 scale.
    timeframe (str): Signal relevance timeframe ('1D', '1W', '1M', '1Q')
}
```

An example given below -

```python
{
    "summary": "AAPL net revenue decreased from 10 Aug 2024 to 12 Dec 2024.",
    "symbol": "AAPL",
    "topics": ["income statement", "net revenue"],
    "sentiment": "Sell",
    "rating": 8,
    "timeframe": "1Q"
}
```

#### Step 3: Expand Your Approach

- Propose **three ways** to scale or innovate on this approach with more compute resources and time.
- Focus on enhancing performance, insights, or the scope of analysis.
- Limit each point to **one line**.

---

### Deliverables

- A single Python script (`financial_signal_generator.py`) that:
  1. Fetches financial data for one company (e.g., AAPL).
  2. Processes the data to generate SIGNALs for all metrics.
  3. Outputs example SIGNALs to the console or a JSON file.
  4. A short write-up at the bottom listing three ideas to expand the solution.

---

### Evaluation Criteria

| Section                       | Weight  | Criteria                                                            |
| ----------------------------- | ------- | ------------------------------------------------------------------- |
| **Step 3: Expansion Plan**    | **50%** | Creativity, innovation, and scalability of ideas.                   |
| **Step 2: SIGNAL Generation** | **30%** | Accuracy and creativity in processing data, sentiment, and ratings. |
| **Step 1: Data Extraction**   | **15%** | Correctness, error handling, and API integration.                   |
| **Performance & Security**    | **5%**  | Use of parallel processing and secure handling of API keys.         |

# finance-script

# enpoints response example

1. balance sheet : https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?period=annual&limit=2&apikey=tmIIs05kYebFj37cmQkKhdoP2L8R502Z

```json
[
  {
    "date": "2020-09-26",
    "symbol": "AAPL",
    "reportedCurrency": "USD",
    "cik": "0000320193",
    "fillingDate": "2020-10-30",
    "acceptedDate": "2020-10-29 18:06:25",
    "calendarYear": "2020",
    "period": "FY",
    "cashAndCashEquivalents": 38016000000,
    "shortTermInvestments": 52927000000,
    "cashAndShortTermInvestments": 90943000000,
    "netReceivables": 37445000000,
    "inventory": 4061000000,
    "otherCurrentAssets": 11264000000,
    "totalCurrentAssets": 143713000000,
    "propertyPlantEquipmentNet": 45336000000,
    "goodwill": 0,
    "intangibleAssets": 0,
    "goodwillAndIntangibleAssets": 0,
    "longTermInvestments": 100887000000,
    "taxAssets": 0,
    "otherNonCurrentAssets": 33952000000,
    "totalNonCurrentAssets": 180175000000,
    "otherAssets": 0,
    "totalAssets": 323888000000,
    "accountPayables": 42296000000,
    "shortTermDebt": 15229000000,
    "taxPayables": 0,
    "deferredRevenue": 6643000000,
    "otherCurrentLiabilities": 41224000000,
    "totalCurrentLiabilities": 105392000000,
    "longTermDebt": 107049000000,
    "deferredRevenueNonCurrent": 0,
    "deferredTaxLiabilitiesNonCurrent": 0,
    "otherNonCurrentLiabilities": 46108000000,
    "totalNonCurrentLiabilities": 153157000000,
    "otherLiabilities": 0,
    "capitalLeaseObligations": 9842000000,
    "totalLiabilities": 258549000000,
    "preferredStock": 0,
    "commonStock": 50779000000,
    "retainedEarnings": 14966000000,
    "accumulatedOtherComprehensiveIncomeLoss": -406000000,
    "othertotalStockholdersEquity": 0,
    "totalStockholdersEquity": 65339000000,
    "totalEquity": 65339000000,
    "totalLiabilitiesAndStockholdersEquity": 323888000000,
    "minorityInterest": 0,
    "totalLiabilitiesAndTotalEquity": 323888000000,
    "totalInvestments": 153814000000,
    "totalDebt": 122278000000,
    "netDebt": 84262000000,
    "link": "https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/0000320193-20-000096-index.htm",
    "finalLink": "https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm"
  }
]
```

2. income statement : https://financialmodelingprep.com/api/v3/income-statement/AAPL?period=annual&limit=2&apikey=tmIIs05kYebFj37cmQkKhdoP2L8R502Z

```json
[
  {
    "date": "2024-09-28",
    "symbol": "AAPL",
    "reportedCurrency": "USD",
    "cik": "0000320193",
    "fillingDate": "2024-11-01",
    "acceptedDate": "2024-11-01 06:01:36",
    "calendarYear": "2024",
    "period": "FY",
    "revenue": 391035000000,
    "costOfRevenue": 210352000000,
    "grossProfit": 180683000000,
    "grossProfitRatio": 0.4620634982,
    "researchAndDevelopmentExpenses": 31370000000,
    "generalAndAdministrativeExpenses": 0,
    "sellingAndMarketingExpenses": 0,
    "sellingGeneralAndAdministrativeExpenses": 26097000000,
    "otherExpenses": 0,
    "operatingExpenses": 57467000000,
    "costAndExpenses": 267819000000,
    "interestIncome": 0,
    "interestExpense": 0,
    "depreciationAndAmortization": 11445000000,
    "ebitda": 134661000000,
    "ebitdaratio": 0.3443707085,
    "operatingIncome": 123216000000,
    "operatingIncomeRatio": 0.3151022287,
    "totalOtherIncomeExpensesNet": 269000000,
    "incomeBeforeTax": 123485000000,
    "incomeBeforeTaxRatio": 0.3157901467,
    "incomeTaxExpense": 29749000000,
    "netIncome": 93736000000,
    "netIncomeRatio": 0.2397125577,
    "eps": 6.11,
    "epsdiluted": 6.08,
    "weightedAverageShsOut": 15343783000,
    "weightedAverageShsOutDil": 15408095000,
    "link": "https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/0000320193-24-000123-index.htm",
    "finalLink": "https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/aapl-20240928.htm"
  }
]
```

3. cash flow statement : https://financialmodelingprep.com/api/v3/cash-flow-statement/AAPL?period=annual&limit=2&apikey=tmIIs05kYebFj37cmQkKhdoP2L8R502Z

```json
[
  {
    "date": "2024-09-28",
    "symbol": "AAPL",
    "reportedCurrency": "USD",
    "cik": "0000320193",
    "fillingDate": "2024-11-01",
    "acceptedDate": "2024-11-01 06:01:36",
    "calendarYear": "2024",
    "period": "FY",
    "netIncome": 93736000000,
    "depreciationAndAmortization": 11445000000,
    "deferredIncomeTax": 0,
    "stockBasedCompensation": 11688000000,
    "changeInWorkingCapital": 3651000000,
    "accountsReceivables": -5144000000,
    "inventory": -1046000000,
    "accountsPayables": 6020000000,
    "otherWorkingCapital": 3821000000,
    "otherNonCashItems": -2266000000,
    "netCashProvidedByOperatingActivities": 118254000000,
    "investmentsInPropertyPlantAndEquipment": -9447000000,
    "acquisitionsNet": 0,
    "purchasesOfInvestments": -48656000000,
    "salesMaturitiesOfInvestments": 62346000000,
    "otherInvestingActivites": -1308000000,
    "netCashUsedForInvestingActivites": 2935000000,
    "debtRepayment": -5998000000,
    "commonStockIssued": 0,
    "commonStockRepurchased": -94949000000,
    "dividendsPaid": -15234000000,
    "otherFinancingActivites": -5802000000,
    "netCashUsedProvidedByFinancingActivities": -121983000000,
    "effectOfForexChangesOnCash": 0,
    "netChangeInCash": -794000000,
    "cashAtEndOfPeriod": 29943000000,
    "cashAtBeginningOfPeriod": 30737000000,
    "operatingCashFlow": 118254000000,
    "capitalExpenditure": -9447000000,
    "freeCashFlow": 108807000000,
    "link": "https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/0000320193-24-000123-index.htm",
    "finalLink": "https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/aapl-20240928.htm"
  }
]
```
