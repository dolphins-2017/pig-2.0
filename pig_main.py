import random, uuid

class Player:
	
	def __init__(self, name):
		self._id = uuid.uuid4().hex
		self.name = name
		self.score = 0


class Turn:

	def __init__(self, player):
		self.player = player
		self.score = 0
		self.can_bank = True
		self.is_active = True

		self.run()


	def run(self):
		while self.is_active:
			command = self.action_selection()
			if command in ('r', 'roll'):
				self.roll()
			elif command in ('b', 'bank') and self.can_bank:
				self.bank()
				print(self.player.name, " total score:", self.player.score)
			elif command in ('b', 'bank') and not self.can_bank:
				print("You cannot bank now, please choose r!")


	def action_selection(self):
		is_valid = False
		while not is_valid:
			command = input("Enter r for roll, b for bank:\n")
			if command not in ("r", "b", "bank", "roll"):
				print("'{}' is not a valid choice.".format(command))
			else:
				is_valid = True
		return command.lower()


	def bank(self):
		self.player.score += self.score
		self.is_active = False


	def roll(self):
		result_dice, roll_score = self._dice_sim()
		self.score += roll_score
		
		print(self.player.name, " rolled: ", *result_dice)
		
		if result_dice.count(1) == 2:
			
			self._snake_eyes()

		elif result_dice[0] == result_dice[1]:
			
			self._doubles(roll_score)
			
		elif result_dice[0] == 1 or result_dice[1] == 1:
			
			self._pig()

		else:

			self._default(roll_score)


	def _pig(self):
		print("Pig!")
		self.score = 0
		self.is_active = self.can_bank = False
		print(self.player.name, " total score:", self.player.score)


	def _snake_eyes(self):
		print("Snake-eyes!")
		self.player.score = 0
		self.score = 0
		self.can_bank = self.is_active = False
		print(self.player.name, " total score:", self.player.score)


	def _doubles(self, roll_score):
		print("Doubles!")
		self.can_bank = False
		print("Roll Score:", roll_score)
		print("Trun Score:", self.score)
		print("Game Score:", self.player.score, "\n")


	def _default(self, roll_score):
		self.can_bank = True
		print("Roll Score:", roll_score)
		print("Trun Score:", self.score)
		print("Game Score:", self.player.score, "\n")


	def _dice_sim(self):
		res_list = [random.randrange(1, 6) for i in range(2)]
		return res_list, sum(res_list)


class Game:
	
	def __init__(self, score_cap):
		self.players = []
		self.log = []
		self.score_cap = score_cap

	def play(self):
		self.setup()
		self.run()

	def run(self):
		
		current_player_idx = len(self.players) - 1

		while not self.is_game_over():
			current_player_idx = (current_player_idx + 1) % len(self.players)
			player = self.players[current_player_idx]
			print("{} it is your turn. Your current score is {}".format(player.name, player.score))
			
			self.log.append(Turn(player))

		winner = self.log[-1].player
		print("Congratulations {}!!!  You Win!!!".format(winner.name))

	def setup(self):
		player_count = self.get_number_of_players()
		for i in range(player_count):
			self.add_player("Player #{}".format(i + 1))
		

	def get_number_of_players(self):
		is_valid = False
		while not is_valid:
			player_count = input("How many players?\n")
			if not player_count.isnumeric():
				print("'{}' is not a whole number.\n Please enter a whole number.".format(player_count))
			else:
				is_valid = True
		return int(player_count.strip())

	def add_player(self, title):
		name = ""
		while not name:
			name = input("{}, please enter your name: ".format(title))
			name = name.strip()
		self.players.append(Player(name))


	def is_game_over(self):
		return any(player.score >= self.score_cap for player in self.players)




def main():
	has_stopped_playing = False

	prompt = "Would you like to play PIG?(Y/N)"
	while not has_stopped_playing:	
		choice = input(prompt).strip().lower()
		while choice not in ("yes", "no", "y", "n"):
			print("'{}' is not a valid choice. \n Please enter yes or no when prompted.".format(choice))
			choice = input(prompt).strip().lower()

		if choice in ("yes", "y"):
			max_score = input("What score would you like to play to?(Please enter a whole number greater than 0)\n")
			while not max_score.isnumeric() or int(max_score) < 1:
				max_score = input("'{}' is not a vaild option. Please enter a whole number greater than 0 below.".format(max_score)).strip()

			game = Game(int(max_score))
			game.play()
			prompt = "Would you like to play PIG again?(Y/N)"
		else:
			has_stopped_playing = True
			print("Thanks for playing!!")

if __name__ == '__main__':
	main()
