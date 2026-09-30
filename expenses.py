from data import expenses
from data import budget
def add_expenses():
    date=input("enter date:")
    category=input("enter category:")
    description=input("enter description:")
    amount=float(input("enter amount:Rs"))
    expense=[date,category,description,amount]
    expenses.append(expense)
def view_expenses():
    if len(expenses)==0:
        print("no expenses found ")
        return
    for expense in expenses:
        print("date:",expense[0],"\ncategory:",expense[1],"\ndescription:",expense[2],"\namount:",expense[3])
