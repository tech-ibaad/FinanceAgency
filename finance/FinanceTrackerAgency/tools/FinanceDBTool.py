from agency_swarm.tools import BaseTool
from pydantic import Field
import sqlite3

class FinanceDBTool(BaseTool):
    """
    A tool for interacting with an SQLite database to manage financial transactions.
    """

    action: str = Field(..., description="Action to perform: 'add', 'get_all', 'get_by_category', 'get_by_date', 'sum_by_category', 'update', 'delete'.")
    date: str = Field(None, description="Transaction date (YYYY-MM-DD). Required for 'add' and 'get_by_date'.")
    category: str = Field(None, description="Transaction category. Required for 'add' and 'get_by_category'.")
    amount: float = Field(None, description="Transaction amount. Required for 'add' and 'update'.")
    description: str = Field(None, description="Description of the transaction. Optional for 'add' and 'update'.")
    transaction_id: int = Field(None, description="ID of the transaction. Required for 'update' and 'delete'.")

    def run(self):
        db_path = "setup/finance_tracker.db"
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        try:
            if self.action == "add":
                cursor.execute("INSERT INTO transactions (date, category, amount, description) VALUES (?, ?, ?, ?)",
                               (self.date, self.category, self.amount, self.description))
                connection.commit()
                result = "✅ Transaction added successfully."

            elif self.action == "get_all":
                cursor.execute("SELECT * FROM transactions")
                result = cursor.fetchall()

            elif self.action == "get_by_category":
                cursor.execute("SELECT * FROM transactions WHERE category = ?", (self.category,))
                result = cursor.fetchall()

            elif self.action == "get_by_date":
                cursor.execute("SELECT * FROM transactions WHERE date = ?", (self.date,))
                result = cursor.fetchall()

            elif self.action == "sum_by_category":
                cursor.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
                result = cursor.fetchall()

            elif self.action == "update":
                cursor.execute("UPDATE transactions SET date = ?, category = ?, amount = ?, description = ? WHERE id = ?",
                               (self.date, self.category, self.amount, self.description, self.transaction_id))
                connection.commit()
                result = "✅ Transaction updated successfully."

            elif self.action == "delete":
                cursor.execute("DELETE FROM transactions WHERE id = ?", (self.transaction_id,))
                connection.commit()
                result = "✅ Transaction deleted successfully."

            else:
                result = "❌ Invalid action specified."

        except Exception as e:
            result = f"❌ Error: {str(e)}"
        
        connection.close()
        return result
