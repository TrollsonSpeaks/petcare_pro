# PetCare Pro 🐾

A robust command-line pet care manager for multi-species households that orchestrates daily routines, health tracking, and time-sensitive tasks. It centralizes species-specific care profiles, schedules recurring feedings and medications, and logs weight, notes, and vet visits with searchable history. Designed around a real household of three parrots and a rabbit, the tool generalizes to any pets with customizable profiles.

Features include a fast, discoverable CLI with human-friendly commands and persistent storage via JSON.

## Features

### 🦜 Multi-Species Pet Management
- Customized care tracking for birds vs rabbits
- Species-specific health monitoring
- Individual pet profiles with special needs

### 📅 Daily Care Logging
- Quick-log common activities (feeding, cleaning, playtime)
- Morning routines, medication reminders, poo patrol
- Time tracking and detailed notes

### 🏥 Health & Medical Tracking
- Medication logging (especially Gus's daily afternoon meds)
- Health observations (Munchkin's feathers, Bailey's arthritis)
- Grooming appointment scheduling

### 💰 Expense Tracking
- Track vet bills, food costs, supplies, toys
- Categorized spending analysis
- Monthly summaries

### 📊 Reports & Analytics
- Weekly care summaries
- Pet activity overviews
- Full dashboard with key metrics

## My Learning Journey
This is my capstone project for Boot.dev! 🚀

### Motivation
Building a complex CLI application with multiple modules
JSON data persistence and file management
Object-oriented programming with interconnected classes
User experience design for command-line interfaces
Project planning and feature prioritization

### Usage
Python programming
File I/O operations
Data structures and algorithms
Error handling
Code organization and modularity

### Contributing Future Enhancements
Web interface for easier mobile access
Photo upload for pet timeline
Integration with vet clinic APIs
Automated reminders via notifications

Built with ❤️  for Bailey, Munchkin, Gus, and Bunion

## Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/petcare_pro.git
cd petcare_pro

# Run the application
python3 main.py

# Requirements
Python 3.6+
No external dependencies (uses only Python standard library)

# Project Structure
petcare_pro/
├── main.py              # Main application entry point
├── pet_manager.py       # Pet profiles and management
├── care_logger.py       # Daily care activity logging
├── health_tracker.py    # Health and medical records
├── expense_tracker.py   # Financial tracking
├── reports.py          # Analytics and reporting
├── data/               # JSON data storage
└── README.md
