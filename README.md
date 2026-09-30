Library
/
README.md



Expense & Budget Manager
Project Title
Expense & Budget Manager

Overview
Expense & Budget Manager is a simple Python-based console application designed to help users record and manage their daily expenses and monthly budget.

The project allows a user to set a monthly budget, add expenses, view all recorded expenses, calculate total spending, check the remaining budget, and search expenses by category.

This project is developed as a 1st-semester Python project using basic programming concepts such as variables, input/output, lists, functions, loops, and conditional statements.

Features
 .Set a monthly budget.

 .Add an expense with:

   .Date

   .Category

   .Description

   . Amount

 .View all recorded expenses.

 .Calculate total expenses.

 .Display the remaining budget.

 .Search expenses by category.

 .Display the total amount spent in a selected category.

 .Simple menu-driven console interface.

 .Handles invalid menu choices.

Technologies / Tools Used
 .Programming Language: Python 3

 .Concepts Used: Variables, data types, input/output, lists, functions, if-elif-else, for loop, while loop, string methods, arithmetic operations.

 .Development Tool: Any Python-supported IDE/editor such as VS Code, IDLE, PyCharm, or similar.

 .Version Control: Git and GitHub.

Project Structure
Expense-Budget-Manager/
│
├── main.py
├── README.md
├── statement.md
└── screenshots/
    └── (optional screenshots)
If the project is divided into multiple Python modules, each module can be placed in the project folder and described in this README.

How to Install and Run
1. Install Python
Install Python 3 from the official Python website or use the Python installation already provided by your college system.

Check the installation using:

python --version
2. Download or Clone the Repository
git clone <your-github-repository-link>
Then open the project folder.

3. Run the Program
python main.py
No external Python libraries are required for the basic version of this project.

How to Use
After running the program, a menu is displayed:

===== EXPENSE & BUDGET MANAGER =====
1. Set Budget
2. Add Expense
3. View Expenses
4. Total Expenses
5. Search by Category
6. Exit
Option 1: Set Budget
Enter the monthly budget amount.

Example:

Enter your monthly budget: ₹10000
Option 2: Add Expense
Enter the date, category, description, and amount.

Example:

Enter date: 29-09-2026
Enter category: Food
Enter description: Lunch
Enter amount: ₹250
Option 3: View Expenses
Displays all expenses entered by the user.

Option 4: Total Expenses
Calculates the total amount spent and, if a budget has been set, displays the remaining budget.

Option 5: Search by Category
Enter a category such as Food, Travel, or Shopping. The program displays matching expenses and the total spent in that category.

Option 6: Exit
Closes the program.

Testing Instructions
The following basic test cases can be used to demonstrate that the program works correctly
Test	Input / Action	Expected Result
Set budget	Enter 10000	Budget is set successfully
Add expense	Food, Lunch, 250	Expense is added
View expenses	Select option 3	Added expense is displayed
Total expenses	Select option 4	Total spending is calculated
Remaining budget	Budget 10000, expense 250	Remaining budget is 9750
Search category	Enter Food	Food expenses are displayed
Invalid choice	Enter 9	Invalid choice message is displayed
Exit	Select option 6	Program terminates
Example Output
===== EXPENSE & BUDGET MANAGER =====
1. Set Budget
2. Add Expense
3. View Expenses
4. Total Expenses
5. Search by Category
6. Exit

Enter your choice: 1
Enter your monthly budget: 10000
Budget set successfully!

Enter your choice: 2
Enter date: 29-09-2026
Enter category: Food
Enter description: Lunch
Enter amount: 250
Expense added successfully!

Enter your choice: 4
Total Expenses: ₹250
Remaining Budget: ₹9750
Concepts Demonstrated
This project demonstrates the following basic Python concepts:
Variables

Integers and floating-point numbers

Strings

Lists

User input using input()

Output using print()

Type conversion using float()

Functions

if, elif, and else

for and while loops

String methods such as lower()

Arithmetic operations

Menu-driven programming

Limitations
Data is stored temporarily while the program is running.

The current basic version does not use a database or external file.

It is a console-based application.

It is intended for educational use and basic personal expense tracking.

Future Enhancements
Possible future improvements include:

Saving expenses permanently in a file.

Using CSV or SQLite for data storage.

Adding edit and delete expense options.

Adding monthly reports.

Adding graphical charts.

Creating a GUI using Tkinter.

Adding login/user accounts.

Screenshots
Screenshots of the running program can be added to the screenshots/ folder. They are optional but recommended for the GitHub repository.

Author
Student Name: PRACHI SHARMA____
Course / Semester: 1st Semester
Subject: Python Programming
Institution: __VIT BHOPAL______

License
This project is created for academic and educational purposes