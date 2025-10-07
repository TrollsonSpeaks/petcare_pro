import json
import os
from datetime import datetime, date

class HealthTracker:
    def __init__(self, data_file='data/health_records.json'):
        self.data_file = data_file
        self.ensure_data_directory()
        self.health_records = self.load_health_records()
    
    def ensure_data_directory(self):
        os.makedirs('data', exist_ok=True)
    
    def load_health_records(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {'medications': [], 'health_observations': [], 'grooming_appointments': []}
        return {'medications': [], 'health_observations': [], 'grooming_appointments': []}
    
    def save_health_records(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.health_records, f, indent=2)
    
    def health_menu(self):
        print("\n🏥 HEALTH & MEDICAL TRACKING:")
        print("=" * 50)
        print("1. Record medication given")
        print("2. Health observation")
        print("3. View health summary")
        print("4. Back to main menu")
        
        choice = input("\nHealth tracking option: ").strip()
        
        if choice == '1':
            self.record_medication()
        elif choice == '2':
            self.log_health_observation()
        elif choice == '3':
            self.view_health_summary()
        elif choice == '4':
            return
    
    def record_medication(self):
        print("\n💊 MEDICATION RECORD:")
        pet_name = input("Pet name: ").strip()
        medication = input("Medication name: ").strip()
        notes = input("Notes (optional): ").strip()
        
        record = {
            'date': date.today().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M'),
            'pet_name': pet_name,
            'medication': medication,
            'notes': notes
        }
        
        self.health_records['medications'].append(record)
        self.save_health_records()
        print(f"✅ Recorded {medication} for {pet_name}")
    
    def log_health_observation(self):
        print("\n👁️ HEALTH OBSERVATION:")
        pet_name = input("Pet name: ").strip()
        observation = input("Observation: ").strip()
        notes = input("Notes: ").strip()
        
        record = {
            'date': date.today().strftime('%Y-%m-%d'),
            'pet_name': pet_name,
            'observation': observation,
            'notes': notes
        }
        
        self.health_records['health_observations'].append(record)
        self.save_health_records()
        print(f"✅ Recorded observation for {pet_name}")
    
    def view_health_summary(self):
        print("\n🏥 HEALTH SUMMARY:")
        print("=" * 50)
        
        if self.health_records['medications']:
            print("Recent Medications:")
            for med in self.health_records['medications'][-5:]:
                print(f"  {med['date']} - {med['pet_name']}: {med['medication']}")
        
        if self.health_records['health_observations']:
            print("\nRecent Observations:")
            for obs in self.health_records['health_observations'][-5:]:
                print(f"  {med['date']} - {obs['pet_name']}: {obs['observation']}")
        
        if not self.health_records['medications'] and not self.health_records['health_observations']:
            print("No health records yet.")

