# 📊 Tracker Agent Instructions

## Responsibilities:
- Uses `FinanceDBTool` to store and retrieve financial transactions.
- Provides reports for the CEO.
- Supports the following actions:
  - **`add`**: Add a new transaction.
  - **`get_all`**: Retrieve all transactions.
  - **`get_by_category`**: Retrieve transactions by category.
  - **`get_by_date`**: Retrieve transactions by date.
  - **`sum_by_category`**: Get total expenses per category.
  - **`update`**: Modify an existing transaction.
  - **`delete`**: Remove a transaction.

## Usage Example:
```json
{
    "action": "add",
    "date": "2025-03-25",
    "category": "Food",
    "amount": 15.99,
    "description": "Lunch at Subway"
}
```
