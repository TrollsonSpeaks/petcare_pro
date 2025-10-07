import json
import os
from datetime import datetime

class PetManager:
    def __init__(self, data_file='data/pets.json'):
        self.data_file = data_file
        self.ensure_data_directory()
        self.pets = self.load_pets()

    def ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        os.makedirs('data', exist_ok=True)

    def load_pets(self):
        """Load pets from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Warning: Could not read pets file. Starting fresh.")
                return {}
        else:
            return self.create_initial_pets()

    def create_initial_pets(self):
        """create your initial pet prfiles"""
        initial_pets = {
            "bailey": {
                "name": "Bailey",
                "species": "Caique",
                "type": "bird",
                "health_notes": "Has arthritis but not currently bothering him",
                "daily_routine": ["morning_wakeup", "snackies", "dinner", "playtime", "bedtime"],
                "special_needs": ["monitor_arthritis"],
                "created_date": datetime.now().strftime('%Y-%m-%d')
            },
            "munchkin": {
                "name": "Munchkin",
                "species": "Hahn's Macaw",
                "type": "bird",
                "health_notes": "Monitor feather condition. Had allergies in past but good this year",
                "daily_routine": ["morning_wakeup", "snackies", "dinner", "playtime", "bedtime"],
                "special_needs": ["feather_check", "allergy_watch"],
                "created_date": datetime.now().strftime('%Y-%m-%d')
            },
            "gus": {
                "name": "Gus",
                "species": "Amazon Parrot",
                "type": "bird",
                "health_notes": "Daily afternoon medication required",
                "daily_routine": ["snackies", "poo_patrol", "food_topup", "afternoon_medication"],
                "special_needs": ["daily_medication"],
                "medication_time": "afternoon",
                "created_date": datetime.now().strftime('%Y-%m-%d')
            },
            "bunion": {
                "name": "Bunion",
                "species": "European Rabbit",
                "type": "rabbit",
                "health_notes": "Regular grooming every 3 months",
                "daily_routine": ["hay_check", "pellet_check", "treats", "playtime"],
                "weekly_routine": ["water_fountain_maintenance", "litter_box_cleaning"],
                "special_needs": ["grooming_every_3_months"],
                "created_date": datetime.now().strftime('%Y-%m-%d')
            }
        }
        self.save_pets(initial_pets)
        return initial_pets

    def save_pets(self, pets_data=None):
        """Save pets to JSON file"""
        data_to_save = pets_data if pets_data else self.pets
        with open(self.data_file, 'w') as f:
            json.dump(data_to_save, f, indent=2)

    def view_all_pets(self):
        """Display all pets with their info"""
        print("\n🐾 YOUR PETS:")
        print("=" * 60)
        
        for pet_id, pet in self.pets.items():
            species_emoji = {"bird": "🦜", "rabbit": "🐰"}.get(pet['type'], "🐾")
            print(f"\n{species_emoji} {pet['name']} ({pet['species']})")
            print(f"   Health Notes: {pet['health_notes']}")
            if pet.get('special_needs'):
                print(f"   Special Needs: {', '.join(pet['special_needs'])}")
            if pet.get('medication_time'):
                print(f"   💊 MEDICATION: {pet['medication_time']}")
                

    def get_pet_by_name(self, name):
        """Find pet by name (case insensitive)"""
        for pet_id, pet in self.pets.items():
            if pet['name'].lower() == name.lower():
                return pet_id, pet
        return None, None

    def get_pets_by_type(self, pet_type):
        """Get all pets of a specific type (bird/rabbit)"""
        return {pid: pet for pid, pet in self.pets.items() if pet['type'] == pet_type}
    
