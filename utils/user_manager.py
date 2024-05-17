from .dice_game import DiceGame
from .user import User

DG_i = DiceGame()

class UserManager:
	Users = {}

	def load_users():
		try:
			with open("users.txt", "r") as f:
				lines = f.readlines()
				for line in lines:
					username, password = line.strip().split(',')
					UserManager.Users[username] = User(username, password)
		except FileNotFoundError:
			print("No user data found.")

	def save_users():
		with open("users.txt", "w") as f:
			for username, user in UserManager.Users.items():
				f.write(f"{username},{user.password}\n")

	def validate_username(self, username):
		if len(username) <4:
			print("Username must be at least 4 characters long.")
			self.register()
		elif username in self.Users:
			print("Username already exists.")
		else:
			return True
	def validate_password(self, password):
		if len(password) <8:
			print("Password must be at least 8 characters long.")
			self.register()
		else:
			return True

	def register(self):
		print("\nRegistration")
		username = input(str("Enter username (at least 4 characters), or leave blank to cancel: "))
		if username == "":
			return
		else:
			if self.validate_username(username):
				password = input(str("Enter password (at least 8 characters), or leave blank to cancel: "))
				if password == "":
					return
				else:
					if self.validate_password(password):
						print("Registration successful.")
						self.Users[username] = User(username, password)
						self.save_users
						return
					
	def login(self):
		print("\nLogin")
		username = input(str("Enter username, or leave blank to cancel: "))
		if username == "":
			return
		else:
			password = input(str("Enter password, or leave blank to cancel: "))
			if password == "":
				return
			elif username in self.Users:
				if password == self.Users[username].password:
					DG_i.menu(username)
					return
				else:
					print("Invalid username/password.")
					self.login()
			else:
				print("Username does not exist.")