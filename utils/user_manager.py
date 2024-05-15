from .user import User

class UserManager:
	def load_users():
		pass

	def save_users():
		pass

	def validate_username():
		pass

	def validate_password():
		pass

	def register():
		username = input(str("Enter username (at least 4 characters), or leave blank to cancel: "))
		if username == "":
			return
		elif len(username) <4:
			print("Username must be at least 4 characters long.")
			return
		password = input(str("Enter password (at least 8 characters), or leave blank to cancel: "))
		if password == "":
			return
		elif len(password) <8:
			print("Password must be at least 8 characters long.")
			return
		else:
			retur
		
	def login():
		pass