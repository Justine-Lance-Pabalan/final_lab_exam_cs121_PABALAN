from utils.user_manager import UserManager

UM_i = UserManager()

def main():
    while True:
        print("\nWelcome to the Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter the number of your choice: ")

        if choice == "1":
            UM_i.register()
        elif choice == "2":
            UM_i.login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()