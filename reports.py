import json
import os
from datetime import datetime, date, timedelta
from collections import Counter

class ReportGenerator:
    def __init__(self, care_file='data/daily_care.json', health_file='data/health_records.json', expense_file='data/expenses.json'):
        self.care_data = self.load_json(care_file)
        self.health_data = self.load_json(health_file)
        self.expense_data = self.load_json(expense_file)
    
    def load_json(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def reports_menu(self):
        print("\n📊 REPORTS & ANALYTICS:")
        print("=" * 40)
        print("1. Weekly care summary")
        print("2. Pet activity overview")
        print("3. Health tracking summary")
        print("4. Expense overview")
        print("5. Full dashboard")
        print("6. Back to main menu")
        
        choice = input("\nReport option: ").strip()
        
        if choice == '1':
            self.weekly_care_summary()
        elif choice == '2':
            self.pet_activity_overview()
        elif choice == '3':
            self.health_summary()
        elif choice == '4':
            self.expense_overview()
        elif choice == '5':
            self.full_dashboard()
        elif choice == '6':
            return
    
    def weekly_care_summary(self):
        print("\n📅 WEEKLY CARE SUMMARY:")
        print("=" * 50)
        
        # Get last 7 days of data
        today = date.today()
        week_dates = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
        
        total_activities = 0
        for date_str in week_dates:
            if date_str in self.care_data:
                day_activities = sum(len(activities) for activities in self.care_data[date_str].values())
                total_activities += day_activities
                print(f"{date_str}: {day_activities} activities logged")
            else:
                print(f"{date_str}: No activities logged")
        
        print(f"\nTotal activities this week: {total_activities}")
        print(f"Average per day: {total_activities/7:.1f}")
    
    def pet_activity_overview(self):
        print("\n🐾 PET ACTIVITY OVERVIEW:")
        print("=" * 50)
        
        pet_counts = {'Bailey': 0, 'Munchkin': 0, 'Gus': 0, 'Bunion': 0}
        
        for date_data in self.care_data.values():
            for pet, activities in date_data.items():
                if pet in pet_counts:
                    pet_counts[pet] += len(activities)
        
        for pet, count in pet_counts.items():
            pet_emoji = "🦜" if pet in ["Bailey", "Munchkin", "Gus"] else "🐰"
            print(f"{pet_emoji} {pet}: {count} activities logged")
    
    def full_dashboard(self):
        print("\n" + "="*60)
        print("🐾 PETCARE PRO DASHBOARD")
        print("="*60)
        
        # Quick stats
        total_days_logged = len(self.care_data)
        total_activities = sum(sum(len(activities) for activities in day_data.values()) for day_data in self.care_data.values())
        
        health_records = 0
        if isinstance(self.health_data, dict):
            for record_type in self.health_data.values():
                if isinstance(record_type, list):
                    health_records += len(record_type)
        
        total_expenses = len(self.expense_data) if isinstance(self.expense_data, list) else 0
        expense_total = sum(e.get('amount', 0) for e in self.expense_data) if isinstance(self.expense_data, list) else 0
        
        print(f"📅 Days with logged activities: {total_days_logged}")
        print(f"🎯 Total care activities: {total_activities}")
        print(f"🏥 Health records: {health_records}")
        print(f"💰 Expenses tracked: {total_expenses} (${expense_total:.2f})")
        
        print(f"\n🦜 Your Birds: Bailey (Caique), Munchkin (Hahn's Macaw), Gus (Amazon)")
        print(f"🐰 Your Rabbit: Bunion (European Rabbit)")
        
        print(f"\n⚠️  Daily Reminders:")
        print(f"   💊 Gus needs afternoon medication")
        print(f"   🦜 Check Munchkin's feather condition")
        print(f"   🦜 Monitor Bailey's arthritis")
        print(f"   🐰 Bunion's grooming every 3 months")
