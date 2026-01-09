import json, os, sys
from datetime import datetime

# Path management
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Configuration
DATA_FILE = "project_status.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "project_name": "New Viral Product Launch",
            "why": "Enter your motivation here...",
            "whats_next": ["Step 1", "Step 2"],
            "last_updated": ""
        }
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def display_status(data):
    print("\n" + "="*40)
    print(f"🚀 PROJECT: {data['project_name']}")
    print("="*40)
    
    print(f"\n💡 WHY WE ARE DOING THIS:")
    print(f"   {data['why']}")
    
    print(f"\n📝 WHATS NEXT:")
    for i, step in enumerate(data['whats_next'], 1):
        print(f"   {i}. {step}")
    
    print("\n" + "-"*40)
    print(f"Last sync: {data['last_updated']}")
    print("-"*40 + "\n")

def update_mode():
    data = load_data()
    print("--- Update Project Compass ---")
    data['why'] = input("Why are we doing this? ")
    steps = input("Enter next steps (separated by commas): ")
    data['whats_next'] = [s.strip() for s in steps.split(",")]
    save_data(data)
    print("✅ Compass updated.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--edit":
        update_mode()
    else:
        display_status(load_data())