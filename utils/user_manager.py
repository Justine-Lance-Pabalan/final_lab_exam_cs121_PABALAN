from .user import User

U_i = User

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
		print("Registration")
		username = input(str("\nEnter username (at least 4 characters), or leave blank to cancel: "))
		if username == "":
			return
		else:
			if self.validate_username(username):
				password = input(str("Enter password (at least 8 characters), or leave blank to cancel: "))
				if password == "":
					return
				elif username in self.Users:
					print("Username already exists")
				else:
					if self.validate_password(password):
						print("Registration successful")
						self.Users[username] = password
						return
					
	def login(self):
			pass