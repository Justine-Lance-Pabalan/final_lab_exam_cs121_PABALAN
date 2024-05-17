from .score import Score

import datetime
import os
import random

S_i = Score

class DiceGame:
	user_scores = {}

	points = 0
	wins = 0

	def load_scores(self):
		try:
			with open("rankings.txt", "r") as file:
				lines = file.readlines()
				for line in lines:
					username, points, stages_won, date = line.strip().split(',')
					self.user_scores[username] = Score(username, int(points), int(stages_won), date)
		except FileNotFoundError:
			print("No score data found.")

	def save_scores(self):
		with open("rankings.txt", "w") as file:
			for score in self.user_scores.values():
				file.write(f"{score.username},{score.points},{score.stages_won},{score.date}\n")

	def roll(self):
		return random.randint(1,6)
	
	def game(self,username):
		u_score = 0
		c_score = 0
		wins = 0
		print(f"\nStarting the game as {username}...")
		while u_score <2 and c_score <2:
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
			print(f"You won this stage {username}!")
			u_score += 3
			wins +=1
			DiceGame.points += u_score
		else:
			print(f"You lost this stage {username}")
			wins += 0
			u_score += 0
		return wins
	
	def play_game(self, username, points, wins):
		while True:
			current_wins = self.game(username)
			wins += current_wins
			points_round = 0
			points_round += self.points
			points += points_round
			
			print(f"Total points: {points}, Stages won: {wins}")
			if wins > 0:
				self_points = 0
				DiceGame.points = 0
				try:
					choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
					if choice == '1':
						continue
					elif choice == '0':
						print(f"Game over. Total points: {points}, Stages won: {wins}")
						if wins > 0:
							date = datetime.datetime.now().strftime("%Y/%m/%d")
							self.user_scores[username] = Score(username, points, wins, date)
							self.save_scores()
						break
				except ValueError:
					print("Invalid input. Please Enter 1 for Yes, 0 for No.")
			elif wins == 0:
				print("Game over. You didn't win stages.")
				break

	def show_top_scores(self):
		sorted_scores = sorted(self.user_scores.values(), key=lambda x: x.points, reverse=True)
		print("Top Scores:")
		for i, score in enumerate(sorted_scores[:10], start=1):
			print(f"{i}. {score.username}: Points - {score.points}, Wins - {score.stages_won}, Date - {score.date}")

	def menu(self, username):
		while True:
			print(f"\nWelcome, {username}!")
			print("Menu:")
			print("1. Start game")
			print("2. Show top scores")
			print("3. Logout")

			choice = input("Enter the number of your choice: ")

			if choice == "1":
				self.play_game(username, 0, 0)
			elif choice == "2":
				self.show_top_scores()
			elif choice == "3":
				break
			else:
				print("Invalid choice. Please try again.")