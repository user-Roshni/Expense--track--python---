import csv

def add_expense():
    date = (input("Enter a date (DD-MM-YYYY): "))
    category = input("Enter a category: ")
    amount = float(input("Enter the amount: "))
    note = input("Enter a short note: ")
    # Open CSV file in append mode and write a new row
    with open('Expenses1.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("Expense added successfully.\n")

def view_expenses():
    print("Date | Category | Amount | Note")
    try:
        with open('Expenses1.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No expenses found. Please add an expense first.\n")

def view_summary():
    summary = {}
    try:
        with open('Expenses1.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 3:
                    amount = float(row[2])
                    category = row[1]
                    # total_expense += amount
                    summary[category] = summary.get(category, 0) + amount
        if summary:
            print("Category-wise spending:")
            for cat, amt in summary.items():
                print(f"{cat}: {amt}")
        else:
            print("No expenses to summarize.\n")
    except FileNotFoundError:
        print("No expenses found. Please add an expense first.\n")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
