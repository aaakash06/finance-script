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
    timeframe (str): Signal relevance timeframe ('1D', '1W', '1M', '1Q'
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
