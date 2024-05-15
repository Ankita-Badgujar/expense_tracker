import json
import datetime

def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        datetime.datetime.strptime(date, '%Y-%m-%d')  # Validate date format
        return {'amount': amount, 'date': date, 'category': category, 'description': description}
    except ValueError as e:
        print("Invalid input:", e)
        return None

def save_expense(expense, filename='expenses.json'):
    try:
        with open(filename, 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

    expenses.append(expense)

    with open(filename, 'w') as file:
        json.dump(expenses, file)

def load_expenses(filename='expenses.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def monthly_summary(expenses):
    summary = {}
    for expense in expenses:
        month = datetime.datetime.strptime(expense['date'], '%Y-%m-%d').strftime('%Y-%m')
        if month not in summary:
            summary[month] = 0
        summary[month] += expense['amount']
    return summary

def category_wise_expenses(expenses):
    categories = {}
    for expense in expenses:
        category = expense['category']
        if category not in categories:
            categories[category] = 0
        categories[category] += expense['amount']
    return categories

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            expense = add_expense()
            if expense:
                save_expense(expense)
        elif choice == '2':
            expenses = load_expenses()
            print("Monthly Summary:", monthly_summary(expenses))
        elif choice == '3':
            expenses = load_expenses()
            print("Category-wise Expenses:", category_wise_expenses(expenses))
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
