from flask import Flask, render_template, request, redirect, url_for
from expense import ExpenseManager
from reports import generate_report

app = Flask(__name__)

expense_manager = ExpenseManager()

@app.route('/')
def index():
    expenses = expense_manager.get_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']

        expense_manager.add_expense(date, category, amount, description)
        return redirect(url_for('index'))
    
    return render_template('add_expense.html')

@app.route('/update/<int:expense_id>', methods=['GET', 'POST'])
def update_expense(expense_id):
    expense = expense_manager.get_expense_by_id(expense_id)
    
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']
        
        expense_manager.update_expense(expense_id, date, category, amount, description)
        return redirect(url_for('index'))
    
    return render_template('update_expense.html', expense=expense)

@app.route('/delete/<int:expense_id>')
def delete_expense(expense_id):
    expense_manager.delete_expense(expense_id)
    return redirect(url_for('index'))

@app.route('/report')
def report():
    report_data = generate_report(expense_manager)
    return render_template('report.html', report=report_data)

if __name__ == '__main__':
    app.run(debug=True)