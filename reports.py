def generate_report(expense_manager):
    expenses = expense_manager.get_expenses()
    total_spent = sum(expense[3] for expense in expenses)

    categories = {}
    for expense in expenses:
        category = expense[2]
        amount = expense [3]
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

   
    report_data = {
        'total_spent': total_spent,
        'categories': categories
    }

    return report_data