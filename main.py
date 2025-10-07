from pet_manager import PetManager
from care_logger import CareLogger
from health_tracker import HealthTracker
from expense_tracker import ExpenseTracker
from reports import ReportGenerator

def display_main_menu():
    print("\n" + "="*60)
    print("🐾 PETCARE PRO - Bailey, Munchkin, Gus & Bunion")
    print("="*60)
    print("1. View All Pets")
    print("2. Log Daily Care")
    print("3. View Today's Summary")
    print("4. Health & Medical Tracking")
    print("5. Expense Tracking")
    print("6. Reports & Analytics")
    print("7. Exit")
    print("-"*60)

def main():
    pm = PetManager()
    cl = CareLogger()
    ht = HealthTracker()
    et = ExpenseTracker()
    rg = ReportGenerator()

    while True:
        display_main_menu()
        choice = input("Choose an option (1-9): ").strip()

        if choice == '1':
            pm.view_all_pets()

        elif choice == '2':
            cl.quick_log_menu()

        elif choice == '3':
            cl.view_today_summary()

        elif choice == '4':
            ht.health_menu()

        elif choice == '5':
            et.expense_menu()

        elif choice == '6':
            rg.reports_menu()

        elif choice == '7':
            print("Take good care of Bailey, Munchkin, Gus & Bunion! 🐾")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
