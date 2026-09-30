from data import expenses
from budget import set_budget
def total_expenses(budget):
    total=0
    for expense in expenses:
        total=total+expense[3]
    print("total expenses: Rs",total)
    if budget>0:
        print("remaining budget: Rs ",budget-total)
def search_category():
    category=input("enter the category:")
    total=0
    for expense in expenses:
        if expense[1].lower()==category.lower():
            print("details:",expense[0],"-",expense[2],"-","Rs",expense[3])
            total=total+expense[3]
            print("total spent on:",category, "Rs",total)
        else:
            print("category not found")
            
            
