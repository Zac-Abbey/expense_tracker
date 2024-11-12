import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import argparse
import requests
import tkinter as tk
from tkinter import messagebox


API_KEY = '8e592b53bc533169c924e1de'  # Actual ExchangeRate-API key

def get_exchange_rate(target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{target_currency}/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data.get('conversion_rate', None)
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching exchange rate: {e}")
        return None  # Return None if there's an error

def create_database():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, date TEXT, category TEXT, amount REAL, currency TEXT, amount_in_usd REAL, description TEXT)''')
    conn.commit()
    conn.close()

def add_expense(date, category, amount, currency, description):
    exchange_rate = get_exchange_rate(currency)
    amount_in_usd = amount * exchange_rate if exchange_rate else amount

    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (date, category, amount, currency, amount_in_usd, description) VALUES (?, ?, ?, ?, ?, ?)",
                   (date, category, amount, currency, amount_in_usd, description))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", f"Added expense: {amount} {currency} (converted to {amount_in_usd} USD)")

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    expenses_text = "\n".join(str(exp) for exp in expenses)
    messagebox.showinfo("Expenses", expenses_text)

def total_spending():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    conn.close()
    messagebox.showinfo("Total Spending", f"Total Spending in USD: {total if total else 0}")

def spending_by_category():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    category_spending = cursor.fetchall()
    conn.close()
    return category_spending

def plot_spending_by_category():
    data = spending_by_category()
    if data:
        categories, amounts = zip(*data)
        plt.figure(figsize=(8, 8))
        plt.pie(amounts, labels=categories, autopct='%1.2f%%', startangle=140)
        plt.title('Spending by Category')
        plt.show()
    else:
        messagebox.showinfo("No Data", "No expenses to plot.")

def add_expense_gui():
    date = entry_date.get()
    category = entry_category.get()
    try:
        amount = float(entry_amount.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount")
        return
    currency = entry_currency.get().upper()
    description = entry_description.get()

    add_expense(date, category, amount, currency, description)

def build_gui():
    global entry_date, entry_category, entry_amount, entry_currency, entry_description
    root = tk.Tk()
    root.title("Expense Tracker")

    # customize fonts by specifying font family, size, and style

    # set fore-grond(text) and background colors

    # control the spacing around widgets by adjusting "padx" and "pady" options.
    # (for more flexibility in layout, consider using the grid() method over pack(), as it gives control over row and column positions)

    tk.Label(root, text="Date (YYYY-MM-DD)", font=("Helvetica", 8, "bold"), fg="black", bg="white").grid(row=0, column=0, padx=3, pady=3)
    entry_date = tk.Entry(root)
    entry_date.grid(row=0, column=1, padx=3, pady=3)

    tk.Label(root, text="Category", font=("Helvetica", 8, "bold"), fg="black", bg="white").grid(row=1, column=0, padx=3, pady=3)
    entry_category = tk.Entry(root)
    entry_category.grid(row=1, column=1, padx=3, pady=3)

    tk.Label(root, text="Amount", font=("Helvetica", 8, "bold"), fg="black", bg="white").grid(row=2, column=0, padx=3, pady=3)
    entry_amount = tk.Entry(root)
    entry_amount.grid(row=2, column=1, padx=3, pady=3)

    tk.Label(root, text="Currency (e.g., EUR, GBP)", font=("Helvetica", 8, "bold"), fg="black", bg="white").grid(row=3, column=0, padx=3, pady=3)
    entry_currency = tk.Entry(root)
    entry_currency.grid(row=3, column=1, padx=3, pady=3)

    tk.Label(root, text="Description", font=("Helvetica", 8, "bold"), fg="black", bg="white").grid(row=4, column=0, padx=3, pady=3)
    entry_description = tk.Entry(root)
    entry_description.grid(row=4, column=1, padx=3, pady=3)

    tk.Button(root, text="Add Expense", command=add_expense_gui).grid(row=5, column=1, padx=5, pady=5) #columnspan=4(padx,pady)
    tk.Button(root, text="View Expenses", command=view_expenses).grid(row=6, column=1, padx=5, pady=5)
    tk.Button(root, text="Total Spending", command=total_spending).grid(row=7, column=1, padx=5, pady=5)
    tk.Button(root, text="Plot Spending by Category", command=plot_spending_by_category).grid(row=8, column=1, padx=5, pady=5)

    root.mainloop()

create_database()
build_gui()
