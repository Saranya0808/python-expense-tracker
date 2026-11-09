expenses = []

while True:

    print("\n================================")
    print("          EXPENSE TRACKER")
    print("================================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Monthly Report")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # 1. ADD EXPENSE
    if choice == "1":

        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (DD-MM-YYYY): ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        expenses.append(expense)

        print("\nExpense added successfully!")

    # 2. VIEW EXPENSES
    elif choice == "2":

        if len(expenses) == 0:
            print("\nNo expenses found!")

        else:
            print("\n========== ALL EXPENSES ==========")

            for index, expense in enumerate(expenses):

                print("\nExpense Index:", index)
                print("Amount: ₹", expense["amount"])
                print("Category:", expense["category"])
                print("Description:", expense["description"])
                print("Date:", expense["date"])
                print("--------------------------------")

    # 3. DELETE EXPENSE
    elif choice == "3":

        if len(expenses) == 0:
            print("\nNo expenses available to delete!")

        else:
            print("\nSelect an expense to delete:")

            for index, expense in enumerate(expenses):

                print(index, expense["category"],
                      "-", expense["amount"])

            delete_index = int(input("Enter expense index: "))

            if 0 <= delete_index < len(expenses):

                deleted_expense = expenses.pop(delete_index)

                print("\nExpense deleted successfully!")
                print("Deleted:", deleted_expense)

            else:
                print("Invalid expense index!")

    # 4. MONTHLY EXPENSE REPORT
    elif choice == "4":

        if len(expenses) == 0:
            print("\nNo expenses available for report!")

        else:

            total_expense = 0
            category_expenses = {}

            for expense in expenses:

                total_expense += expense["amount"]

                category = expense["category"]

                if category in category_expenses:
                    category_expenses[category] += expense["amount"]

                else:
                    category_expenses[category] = expense["amount"]

            print("\n========== EXPENSE REPORT ==========")

            print("Total Expenses: ₹", round(total_expense, 2))

            print("Number of Transactions:", len(expenses))

            average = total_expense / len(expenses)

            print("Average Expense: ₹", round(average, 2))

            print("\nCategory-wise Expenses:")

            for category, amount in category_expenses.items():

                print(category, ": ₹", round(amount, 2))

    # 5. EXIT
    elif choice == "5":

        print("\nThank you for using Expense Tracker!")
        break

    # INVALID CHOICE
    else:

        print("\nInvalid choice! Please try again.")
