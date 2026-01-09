import json, os, sys
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "gut_health_status.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        # Default starting data
        return {
            "project_name": "72-Hour Gut Calm",
            "why": "Reset system",
            "whats_next": ["Initial fasting"],
            "platforms": ["N/A"],
            "last_updated": "Now"
        }
    with open(DATA_FILE, "r", encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(DATA_FILE, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    data = load_data()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--edit":
        print("\n--- EDIT MODE ---")
        data['project_name'] = input(f"Project Name [{data['project_name']}]: ") or data['project_name']
        data['why'] = input("Why we are doing this? ")
        
        steps = input("Tasks needed (comma-separated): ")
        data['whats_next'] = [s.strip() for s in steps.split(",")]
        
        platforms = input("Platforms to visit (comma-separated): ")
        data['platforms'] = [p.strip() for p in platforms.split(",")]
        
        save_data(data)
        print("✅ Successfully updated.")
    else:
        # YOUR NEW CUSTOM VIEW START
        print("\n" + "="*40)
        print(f"🚀 PROJECT: {data['project_name']}")
        print("="*40)
        
        print(f"\n💡 WHY WE ARE DOING THIS:")
        print(f"   {data['why']}")
        
        print(f"\n📝 WHAT TASKS ARE NEEDED TO COMPLETE THIS STEP?:")
        for i, step in enumerate(data['whats_next'], 1):
            print(f"   {i}. {step}")
            
        print(f"\n🌐 WHAT PLATFORMS MUST BE VISITED?:")
        # Notice we use data['platforms'] here instead of repeating tasks
        for i, plat in enumerate(data.get('platforms', ['N/A']), 1):
            print(f"   {i}. {plat}")
            
        print("\n" + "-"*40)
        print(f"Last sync: {data['last_updated']}")
        print("-"*40 + "\n")