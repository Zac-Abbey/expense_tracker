# EXPENSE TRACKER WITH CURRENCY CONVERSION

This Python-based expense tracking application allows users to input expenses in various currencies and automatically convert them to USD. The application also includes a pie chart visualization of spending by category.

## Features
- **Add Expenses:** Enter date, category, amount, and description. The app converts the inputted currency to USD automatically.
- **Currency Conversion:** Each expense amount is converted to USD based on real-time exchange rates before being stored in the database.
- **Database Storage:** Expenses are stored in an SQLite database with fields for date, category, amount, currency, USD equivalent, and description.
- **View Expenses:** Display a list of all expenses recorded.
- **Total Spending:** Calculate the total spending in USD.
- **Pie Chart Visualization:** Provides a pie chart showing spending distribution across categories.

## Requirements
    - Python 3.x
    - Tkinter (Included with Python standard library)
    - SQLite3 (Python standard library)
    - Matplotlib (for pie chart visualization)
    - Requests (for fetching exchange rates)
    - Numpy (for enhanced data handling)
**Install the additional libraries via pip:**
    `pip install matplotlib`

## Installation
- **Clone or downLoad the repository:**
        `git clone https://github.com/Zac-Abbey/expense_tracker.git`
- **Navigate to the project directory:**
        `cd expense_tracker`
- **Install the required packages:**
        `pip install -r requirements.txt`

## Usage
**Run the application with:**
    `python currency_expense_tracker.py`

## Main Function
1. **Add Expense**
    - Input date, category, amount, currency, and a description.
    - The amount is converted to USD using an exchange rate API, and both the original and USD amounts are saved to the database.
2. **View Expenses**
    - Displays all recorded expenses with date, category, amount (in the original currency), and converted amount in USD.
3. **Total Spending**
    - Calculates and displays total spending in USD.
4. **Pie Chart Visualization**
    - Shows a pie chart visualizing spending by category.

## Example Usage
- **Add Expense:** Open the app, fill in the date, category (e.g., "Groceries"), amount (e.g., 50), currency (e.g., "EUR"), and description (e.g., "Weekly groceries").
- **View Expenses:** Navigate to "View Expenses" to see all entries.
- **Visualize Spending:** Click on "Show Spending by Category" to display a pie chart of spending across categories.

## Code Structure

### Key Functions
- **get_exchange_rate:** fetches the current exchange rate for the input currency via an API like ExchangeRate-API.
- **create_database:** Initializes the SQLite database with an expenses table.
- **add_expense:** Inserts a new expense entry, converts to USD using get_exchange_rate, and saves both original and converted amounts.
- **view_expenses:** Retrieves and displays all expenses.
- **total_spending:** Computes the total expenses in USD.
- **spending_by_category:** Gathers spending totals per category for the pie chart.
- **plot_spending_by_category:** Generates a pie chart using Matplotlib.
- **build_gui:** Create a user-friendly way for people to interact with the expense tracker.

## Screenshots
1. **Main GUI Window:**
![Main GUI Window]
![Reference Image](/images_c_exp/Main%20GUI%20Window.png)
*Main GUI Window*

2. **Expense List:**
![Expense List]
![Reference Image](/images_c_exp/Expense%20List.png)
*Expense List*

3. **Total Spending:**
![TOTAL SPENDING]
![Reference Image](/images_c_exp/TOTAL%20SPENDING.png)
*Total Spending*

4. **Pie Chart Visualization:**
![Pie Chart Visualization]
![Reference Image](/images_c_exp/Pie%20Chart%20Visualization.png)
*Pie Chart Visualization*

## Acknowledgments
- **Exchange Rate API:** ExchangeRate-API for currency conversion.
- **Matplotlib Documentation:** Matplotlib for charting support.
- **Tkinter Documentation:** Tkinter for GUI.

## License
This project is licensed under the MIT License.

# CONTACT
For questions or issues, please contact zaccheusa123@gmail.com