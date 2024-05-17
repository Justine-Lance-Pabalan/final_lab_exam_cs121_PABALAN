from .user import User
from .score import Score

import datetime
import os
import random

S_i = Score

class DiceGame:
	user_scores = {}

	def load_scores(self):
		pass

	def save_scores(self):
		pass
	
	def roll(self):
		return random.randint(1,6)
	
	def game(self,username):
		u_score = 0
		c_score = 0
		wins = 0
		print(f"Starting the game as {username}...")
		while u_score <2 or c_score <2:
			for rolls in range(1):
				u_roll = self.roll()
				c_roll = self.roll()
			print(f"{username} rolled: ", u_roll)
			print("CPU rolled: ", c_roll)

			if u_roll > c_roll:
				u_score += 1
				print(f"You win this round! {username}.")
			elif c_roll > u_roll:
				c_score += 1
				print("Computer wins this round!")
			else: 
				print("It's a tie!")

		if u_score > c_score:
			print(f"You won this stage {username}.")
			wins += 1
		else:
			print(f"You lost the stage {username}.")

	def play_game(self, username, u_score, wins):
		points = 0
		stages_won = 0
		while True:
			self.game()
			if wins >0:
				u_score += 3
				stages_won += 1
				points += u_score
			elif wins == 0:
				print("Game over. You didn't win stages.")
				break
			
			print(f"Total points: {points}, Stages won: {stages_won}")
			try:
				choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
				if choice == '1':
					continue
				elif choice == '0':
					if wins >0:
						print(f"Game over. Total points: {points}, Stages won: {stages_won}")
						date = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
						self.user_scores[username] = (Score(username, points, stages_won, date))
						self.save_scores()
						self.points = 0
						self.stages_won = 0
						break
			except ValueError:
				print("Invalid input. Please Enter 1 for Yes, 0 for No.")

	def show_top_scores(self):
		pass

	def menu(self, username):
		while True:
			print(f"\nWelcome, {username}!")
			print("Menu:")
			print("1. Start game")
			print("2. Show top scores")
			print("3. Logout")

			choice = input("Enter the number of your choice: ")

			if choice == "1":
				self.play_game()
			elif choice == "2":
				self.show_top_scores()
			elif choice == "3":
				break
			else:
				print("Invalid choice. Please try again.")