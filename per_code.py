def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Travel, Other): ")
    date = input("Enter date (YYYY-MM-DD): ")
    note = input("Enter a short note: ")
    with open('Expenses.xlsv', 'a') as file:
        file.write(f"{amount},{category},{date},{note}\n")

def view_expenses():
    print("Amount | Category | Date | Note")
    with open('expenses.csv', 'r') as file:
        for line in file:
            print(" | ".join(line.strip().split(",")))

def view_summary():
    summary = {}
    with open('expenses.csv', 'r') as file:
        for line in file:
            amount, category, *rest = line.strip().split(",", 3)
            amount = float(amount)
            summary[category] = summary.get(category, 0) + amount
    print("Category-wise spending:")
    for cat, amt in summary.items():
        print(f"{cat}: {amt}")

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
