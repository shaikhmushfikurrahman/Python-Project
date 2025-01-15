import json
import os

# Function to load existing passwords from file
def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            return json.load(file)
    else:
        return {}

# Function to save passwords to file
def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

# Function to add a new password
def add_password(passwords):
    website = input("Enter the website/service name: ")
    username = input("Enter your username/email: ")
    password = input("Enter your password: ")

    # Add the password to the dictionary
    passwords[website] = {"username": username, "password": password}
    save_passwords(passwords)
    print(f"Password for {website} added successfully!")

# Function to display all saved passwords
def display_passwords(passwords):
    if not passwords:
        print("No passwords stored.")
    else:
        for website, creds in passwords.items():
            print(f"Website: {website}")
            print(f"Username: {creds['username']}")
            print(f"Password: {creds['password']}\n")

# Function to search for a password
def search_password(passwords):
    website = input("Enter the website/service name to search: ")
    if website in passwords:
        creds = passwords[website]
        print(f"Website: {website}")
        print(f"Username: {creds['username']}")
        print(f"Password: {creds['password']}\n")
    else:
        print("Password not found for this website.")

# Main function to run the program
def main():
    passwords = load_passwords()

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Display Passwords")
        print("3. Search Password")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_password(passwords)
        elif choice == '2':
            display_passwords(passwords)
        elif choice == '3':
            search_password(passwords)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid option, please try again.")

# Run the program
if __name__ == "__main__":
    main()
