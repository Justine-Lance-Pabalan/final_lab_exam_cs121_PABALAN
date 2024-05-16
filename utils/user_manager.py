from .user import User
from .dice_game import DiceGame

U_i = User
DG_i = DiceGame
class UserManager:
	Users = {}

	def load_users():
		pass

	def save_users():
		pass

	def validate_username(self, username):
		if len(username) <4:
			print("Username must be at least 4 characters long.")
			self.register()
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
				elif username in self.Users:
					print("Username already exists.")
				else:
					if self.validate_password(password):
						print("Registration successful.")
						self.Users[username] = password
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
				if password == self.Users[username]:
					DiceGame.menu(self)
				else:
					print("Invalid username/password.")
					self.login()
			else:
				print("Username does not exist.")