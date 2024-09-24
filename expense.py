import sqlite3
from utils import get_current_date

class ExpenseManager:
    def __init__(self, db_name='db/expenses.db'):
        # Add check_same_thread=False to allow the connection to be shared between threads
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    date TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL,
                    description TEXT
                )
            ''')

    def add_expense(self, date, category, amount, description):
        with self.conn:
            self.conn.execute('''
                INSERT INTO expenses (date, category, amount, description)
                VALUES (?, ?, ?, ?)
            ''', (date, category, amount, description))

    def get_expenses(self):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM expenses')
            return cursor.fetchall()

    def get_expense_by_id(self, expense_id):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,))
            return cursor.fetchone()

    def update_expense(self, expense_id, date, category, amount, description):
        with self.conn:
            self.conn.execute('''
                UPDATE expenses
                SET date = ?, category = ?, amount = ?, description = ?
                WHERE id = ?
            ''', (date, category, amount, description, expense_id))

    def delete_expense(self, expense_id):
        with self.conn:
            self.conn.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))

    def __del__(self):
        self.conn.close()

