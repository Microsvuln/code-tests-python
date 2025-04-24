import pickle

class UserData:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def get_role(self):
        return self.role

def main():
    try:
        with open("data.ser", "rb") as file:
            user = pickle.load(file)

        if isinstance(user, UserData):
            if user.get_role() == "admin":
                print("Access granted!")
            else:
                print("Access denied!")
        else:
            print("Invalid object type!")

    except (FileNotFoundError, pickle.UnpicklingError, AttributeError) as e:
        print(f"Error loading file: {e}")

if __name__ == "__main__":
    main()
