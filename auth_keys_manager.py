import json
import os
from typing import Dict, List, Any

def load_existing_auth_keys(filepath: str) -> Dict[str, Any]:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        return {"Users": {}}

def save_auth_keys(filepath: str, data: Dict[str, Any]):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def get_user_choice(prompt: str, choices: List[str]) -> str:
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        print(f"Invalid choice. Please choose from: {', '.join(choices)}")

def get_user_kind() -> str:
    valid_kinds = ["player", "mod", "admin"]
    while True:
        kind = input("UserKind (Player/Mod/Admin): ").strip().lower()
        if kind in valid_kinds:
            return kind.capitalize()
        print(f"Invalid UserKind. Please choose from: {', '.join(valid_kinds)}")

def get_badges() -> List[int]:
    while True:
        badges_input = input("Badges (comma-separated integers, e.g., 0,104): ").strip()
        if not badges_input:
            return []
        try:
            badges = [int(b.strip()) for b in badges_input.split(',')]
            return badges
        except ValueError:
            print("Invalid format. Please enter comma-separated integers (e.g., 0,104)")

def get_tags() -> List[str]:
    tags_input = input("Tags (comma-separated strings, e.g., elite,pvp): ").strip()
    if not tags_input:
        return []
    return [tag.strip() for tag in tags_input.split(',')]

def get_description() -> str:
    return input("Description: ").strip() or ""

def add_user_entry(data: Dict[str, Any]):
    print("\n--- Adding new user entry ---")
    
    key = input("Auth key: ").strip()
    if not key:
        print("Auth key cannot be empty!")
        return False
    
    user_kind = get_user_kind()
    badges = get_badges()
    tags = get_tags()
    description = get_description()
    
    data["Users"][key] = {
        "UserKind": user_kind,
        "Tags": tags,
        "Badges": badges,
        "Description": description
    }
    
    print(f"\nAdded user with key '{key}'")
    return True

def main():
    print("=== Auth Keys Manager ===")
    
    # Question 1: New or existing file
    choice = get_user_choice(
        "Do you want to edit an existing auth_keys.json file or create a new one? (existing/new): ",
        ["existing", "new"]
    )
    
    if choice == "existing":
        filepath = input("Path to existing auth_keys.json: ").strip().strip('"').strip("'")
        if not os.path.exists(filepath):
            print(f"File '{filepath}' does not exist. Creating new file instead.")
            filepath = filepath if filepath.endswith('.json') else f"{filepath}.json"
            data = {"Users": {}}
        else:
            data = load_existing_auth_keys(filepath)
            print(f"Loaded {len(data['Users'])} existing user entries.")
    else:
        filepath = input("Path for new auth_keys.json: ").strip().strip('"').strip("'")
        if os.path.isdir(filepath):
            filepath = os.path.join(filepath, "auth_keys.json")
        elif filepath.endswith('.json'):
            pass
        else:
            filepath = os.path.join(filepath, "auth_keys.json")
        data = {"Users": {}}
    
    while True:
        # Questions 2-6: Add user info
        if not add_user_entry(data):
            continue
        
        # Question 8: Add another option or save
        action = get_user_choice(
            "\nAdd another user or save and exit? (add/save): ",
            ["add", "save"]
        )
        
        if action == "save":
            save_auth_keys(filepath, data)
            print(f"\nSaved auth_keys.json to '{filepath}'")
            print(f"Total users: {len(data['Users'])}")
            break

if __name__ == "__main__":
    main()
