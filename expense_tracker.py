import json
import os
from datetime import datetime, date

class ExpenseTracker:
    def __init__(self, data_file='data/expenses.json'):
        self.data_file = data_file
        self.ensure_data_directory()
        self.expenses = self.load_expenses()
    
    def ensure_data_directory(self):
        os.makedirs('data', exist_ok=True)
    
    def load_expenses(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_expenses(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f, indent=2)
    
    def expense_menu(self):
        print("\n💰 EXPENSE TRACKING:")
        print("=" * 40)
        print("1. Add expense")
        print("2. View recent expenses")
        print("3. Monthly summary")
        print("4. Expense by pet")
        print("5. Back to main menu")
        
        choice = input("\nExpense option: ").strip()
        
        if choice == '1':
            self.add_expense()
        elif choice == '2':
            self.view_recent_expenses()
        elif choice == '3':
            self.monthly_summary()
        elif choice == '4':
            self.expenses_by_pet()
        elif choice == '5':
            return
    
    def add_expense(self):
        print("\n💸 ADD EXPENSE:")
        
        # Quick categories
        print("Common categories:")
        print("1. Food/Treats  2. Vet Visit  3. Grooming  4. Toys  5. Supplies  6. Other")
        
        cat_choice = input("Category (1-6 or type custom): ").strip()
        categories = {'1': 'Food/Treats', '2': 'Vet Visit', '3': 'Grooming', 
                     '4': 'Toys', '5': 'Supplies', '6': 'Other'}
        
        category = categories.get(cat_choice, cat_choice)
        
        pet_name = input("Pet (Bailey/Munchkin/Gus/Bunion or 'All'): ").strip()
        amount = float(input("Amount ($): "))
        description = input("Description: ").strip()
        
        expense = {
            'date': date.today().strftime('%Y-%m-%d'),
            'category': category,
            'pet': pet_name,
            'amount': amount,
            'description': description
        }
        
        self.expenses.append(expense)
        self.save_expenses()
        print(f"✅ Added ${amount:.2f} expense for {pet_name}")
    
    def view_recent_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        print("\n💰 RECENT EXPENSES:")
        print("=" * 50)
        
        # Show last 10 expenses
        for expense in self.expenses[-10:]:
            pet_emoji = "🦜" if expense['pet'] in ["Bailey", "Munchkin", "Gus"] else "🐰" if expense['pet'] == "Bunion" else "🐾"
            print(f"{expense['date']} | {pet_emoji} {expense['pet']} | ${expense['amount']:.2f}")
            print(f"   {expense['category']}: {expense['description']}")
    
    def monthly_summary(self):
        if not self.expenses:
            print("No expenses to summarize.")
            return
        
        current_month = date.today().strftime('%Y-%m')
        monthly_expenses = [e for e in self.expenses if e['date'].startswith(current_month)]
        
        if not monthly_expenses:
            print(f"No expenses for {current_month}")
            return
        
        total = sum(e['amount'] for e in monthly_expenses)
        
        print(f"\n📊 {current_month} SUMMARY:")
        print("=" * 30)
        print(f"Total spent: ${total:.2f}")
        print(f"Number of expenses: {len(monthly_expenses)}")
        
        # By category
        categories = {}
        for expense in monthly_expenses:
            cat = expense['category']
            categories[cat] = categories.get(cat, 0) + expense['amount']
        
        print("\nBy category:")
        for cat, amount in categories.items():
            print(f"  {cat}: ${amount:.2f}")
