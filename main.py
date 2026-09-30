from budget import set_budget
from expenses import add_expenses,view_expenses
from reports import total_expenses,search_category
def main():
    print("1.set budget")
    print("2.add expense")
    print("3.view expense")
    print("4.total expense")
    print("5.search by category")
    print("6.exit")
    while True:
        choice=int(input("eter your choice:"))
        if choice==1:
           set_budget()
        elif choice==2:
           add_expenses()
        elif choice==3:
           view_expenses()
        elif choice==4:
           total_expenses(budget)
        elif choice==5:
           search_category()
        elif choice==6:
           print("thank you")
           break
        else:
           ("invalid choice")
main()
