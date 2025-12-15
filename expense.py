def add_expense():
    Date = input("Enter the date (DD-MM-YYYY) : ")
    Category = input("Enter the category : ")
    Amount = float(input("Enter amount : "))
    Note = input("Give a short note : ")
    with open('Expenses1.csv', 'a') as file:
        file.write(f"{Date},{Category},{Amount},{Note}\n")
add_expense()

def view_expenses():
        print("Date | Category | Amount | Note")
        with open('Expenses1.csv', 'r') as file:
            for line in file:
                print(" | ".join(line.strip().split(",")))
                view_expenses()

