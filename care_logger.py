import json
import os
from datetime import datetime, date

class CareLogger:
    def __init__(self, data_file='data/daily_care.json'):
        self.data_file = data_file
        self.ensure_data_directory()
        self.care_logs = self.load_care_logs()

    def ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        os.makedirs('data', exist_ok=True)

    def load_care_logs(self):
        """Load care logs to JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_care_logs(self):
        """Save care logs to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.care_logs, f, indent=2)

    def log_care_activity(self, pet_name, activity_type, notes="", time_spent=None):
        """Log a care activity for a pet"""
        today = date.today().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime('%H:%m')


        if today not in self.care_logs:
            self.care_logs[today] = {}

        if pet_name not in self.care_logs[today]:
            self.care_logs[today][pet_name] = []

        activity = {
            'activity': activity_type,
            'time': current_time,
            'notes': notes,
            'time_spent': time_spent
        }

        self.care_logs[today][pet_name].append(activity)
        self.save_care_logs()

        print(f"✅ Logged {activity_type} for {pet_name} at {current_time}")

    def quick_log_menu(self):
        """Quick logging menu for common activities"""
        print("\n🦜 BIRD CARE:")
        print("1. Morning wakeup (Bailey & Munchkin)")
        print("2. Give snackies (all birds)")
        print("3. Dinner time (Bailey & Munchkin)")
        print("4. Poo patrol (Gus)")
        print("5. Food top-up (Gus")
        print("6. Gus's afternoon medication 💊")
        print("7. Playtime with birds")

        print("\n🐰 BUNION CARE:")
        print("8. Check/refill hay")
        print("9. Check/refill pellets")
        print("10. Give treats")
        print("11. Playtime with Bunion")
        print("12. Water fountain maintenance")
        print("13. Litter box cleaning")

        print("\n14. Custom activity")
        print("15. Back to main menu")

        choice = input("\nQuick log option: ").strip()

        if choice == '1':
            self.log_care_activity("Bailey", "morning_wakeup")
            self.log_care_activity("Munchkin", "morning_wakeup")
            print("Both little parrots are awake!")

        elif choice == '2':
            notes = input("What snackies today? (optional): ").strip()
            self.log_care_activity("Bailey", "snackies", notes)
            self.log_care_activity("Munchkin", "snackies", notes)
            self.log_care_activity("Gus", "snackies", notes)
            print("All birds got their snackies!")

        elif choice == '3':
            notes = input("What's for dinner? (optional): ").strip()
            self.log_care_activity("Bailey", "dinner", notes)
            self.log_care_activity("Munchkin", "dinner", notes)
            print("Dinner served for the little parrots!")

        elif choice == '4':
            notes = input("Poo patrol notes(optional): ").strip()
            self.log_care_activity("Gus", "poo_patrol", notes)

        elif choice == '5':
            self.log_care_activity("Gus", "food_topup")

        elif choice == '6':
            notes = input("Medication notes (optional): ").strip()
            self.log_care_activity("Gus", "afternoon_medication", notes)
            print("Gus got his afternoon medication!")

        elif choice == '7':
            pet_name = input("Playtime with which bird? (Bailey/Munchkin/Gus): ").strip()
            duration = input("How long? (optinoal): ").strip()
            notes = input("What did you play? (optional): ").strip()
            self.log_care_activity(pet_name, "playtime", notes, duration)

        elif choice == '8':
            self.log_care_activity("Bunion", "hay_check")

        elif choice == '9':
            self.log_care_activity("Bunion", "pellet_check")

        elif choice == '10':
            notes = input("What treats? (optional): ").strip()
            self.log_care_activity("Bunion", "treats", notes)

        elif choice == '11':
            duration = input("How long did you play? (optional): ").strip()
            notes = input("What did you do? (optional): ").strip()
            self.log_care_activity("Bunion", "playtime", notes, duration)

        elif choice == '12':
            notes = input("What maintenance? (battery/filters/cleaning): ").strip()
            self.log_care_activity("Bunion", "water_fountain_maintenance", notes)

        elif choice == '13':
            self.log_care_activity("Bunion", "litter_box_cleaning")

        elif choice == '14':
            pet_name = input("Pet name: ").strip()
            activity = input("Activity: ").strip()
            notes = input("Notes (optional): ").strip()
            self.log_care_activity(pet_name, activity, notes)

        elif choice == '15':
            return
        else:
            print("Invalid choice.")

    def view_today_summary(self):
        """Show today's care activities"""
        today = date.today().strftime('%Y-%m-%d')

        if today not in self.care_logs:
            print(f"\nNo activities logged for today ({today})")
            return

        print(f"\nTODAY'S CARE SUMMARY ({today}):")
        print("=" * 50)

        for pet_name, activities in self.care_logs[today].items():
            pet_emoji = "🦜" if pet_name in ["Bailey", "Munchkin", "Gus"] else "🐰"
            print(f"\n{pet_emoji} {pet_name}:")
            for activity in activities:
                time_info = f" ({activity['time_spent']})" if activity.get('time_spent') else ""
                notes_info = f" - {activity['notes']}" if activity.get('notes') else ""
                print(f"   {activity['time']} - {activity['activity']}{time_info}{notes_info}")
