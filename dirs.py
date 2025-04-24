import os
import re

BASE_DIRECTORY = "/var/www/html/user_files/"

def authenticate_user(username):
    """Dummy authentication logic"""
    return bool(username.strip())

def is_valid_file_name(file_name):
    """Validate file name to prevent directory traversal"""
    return bool(re.match(r"^[a-zA-Z0-9_\-]+\.[a-zA-Z0-9]+$", file_name))

def display_file_content(file_path):
    """Read and display file content securely"""
    try:
        # Ensure the file path is within the base directory
        real_base = os.path.realpath(BASE_DIRECTORY)
        real_path = os.path.realpath(file_path)

        if not real_path.startswith(real_base):
            print("Access denied: Invalid file path.")
            return

        if not os.path.exists(file_path):
            print("File not found.")
            return

        # Read and display file content
        print("\nFile Content:")
        with open(file_path, "r") as file:
            for line in file:
                print(line, end="")

    except Exception as e:
        print("An error occurred while reading the file.")
        print(e)

def display_user_statistics(username):
    """Dummy user statistics"""
    print(f"\nUser Statistics for {username}:")
    print("Total Files: 15")
    print("Last Login: 2023-10-01")

def main():
    print("Welcome to the File Management System!")
    username = input("Enter your username: ").strip()

    if not authenticate_user(username):
        print("Authentication failed. Exiting...")
        return

    file_name = input("Enter the name of the file you want to view: ").strip()

    if not is_valid_file_name(file_name):
        print("Invalid file name.")
        return

    # Construct the file path safely
    file_path = os.path.join(BASE_DIRECTORY, username, file_name)

    display_file_content(file_path)
    display_user_statistics(username)

if __name__ == "__main__":
    main()
