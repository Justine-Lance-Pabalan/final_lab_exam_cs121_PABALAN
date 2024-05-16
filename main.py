from utils.dice_game import DiceGame
from utils.user_manager import UserManager
from utils.user import User
from utils.score import Score

UM_i = UserManager()
U_i = User()

def main():
    while True:
        print(f"Welcome to the Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            UM_i.register()
        elif choice == "2":
            UM_i.login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
            return

main()