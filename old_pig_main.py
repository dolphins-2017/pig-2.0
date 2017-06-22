import random, uuid

class Player:
	def __init__(self, name):
		self.name = name
		self._id = uuid.uuid4().hex
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
			command = self.prompt_player()
			if command in ('r', 'roll'):
				self.roll()	
			elif command in ('b', 'bank') and self.can_bank:
				self.bank()
			elif command in ('b', 'bank') and not self.can_bank:
				print("You cannot bank now, please choose r!")
			
			print("="*80)

	def prompt_player(self):
		is_valid = False
		while not is_valid:
			response = input("Enter r for roll, b for bank:\n").strip().lower()
			if response in ("r", "b", "roll", "bank"):
				command = response
				is_valid = True
			else:
				print("'{}' is not a valid option.".format(response))
		return command	


	def bank(self):
		self.player.score += self.score
		self.can_bank = False
		self.is_active = False
		print(self.player.name, " total score:", self.player.score)


	def roll(self):
		result_dice = self._dice_sim()
		roll_score = sum(result_dice)

		self.score += roll_score
		
		print(self.player.name, " Result: ", *result_dice)
		
		if(result_dice[0] == result_dice[1]) and (result_dice[0] == "1"):
			# handles snake_eyes
			self._snake_eyes()
		
		elif(result_dice[0] == result_dice[1]):
			# handles doubles
			self.doubles(roll_score)

		elif(result_dice[0] == 1) or (result_dice[1] == 1):
			# handles pig
			self._pig()

		else:
			# default
			self._default(roll_score)

	
	def _snake_eyes(self):
		self.score = 0
		self.can_bank = False
		self.is_active = False

		self.player.score = 0
		print("Snake-eyes!")
		print(self.player.name, " total score:", self.player.score)

	
	def _pig(self):
		self.score = 0
		self.can_bank = False
		self.is_active = False

		print("Pig!")
		print(self.player.name, " total score:", self.player.score)

	
	def _doubles(self, roll_score):
		self.can_bank = False
		
		print("Doubles!")
		print("Roll Score:", roll_score)
		print("Current Score:", self.score, "\n")


	def _default(self, roll_score):
		self.can_bank = True
		print("Roll Score:", roll_score)
		print("Current Score:", self.player.score, "\n")


	def _dice_sim(self):
		return [random.randrange(1, 6) for _ in range(2)]


class Game:

	def __init__(self):
		self.max_score = 0
		self.player_count = 0
		self.players = []
		self.log = []
		self.turn_count = 0
		self.is_active = True

	def run(self):
		self.setup()
		self.play()

	def setup(self):
		self.display_instructions()
		self.set_max_score()
		self.set_number_or_players()
		
		for _ in range(self.player_count):
			self.add_player()

	def play(self):
		while self.is_active:
			player = self.players[self.turn_count%len(self.players)]
			self.log.append(Turn(player))
			self.end_turn()

	def set_max_score(self):
		is_valid = False
		while not is_valid:
			response = input("Please set the max score(Enter a whole number):\n").strip()
			if response.isnumeric():
				self.max_score = int(response)
				is_valid = True
			else:
				print("'{}' is not a whole number.".format(response))


	def set_number_or_players(self):
		is_valid = False
		while not is_valid:
			response = input("Please set the number of players(Enter a whole number):\n").strip()
			if response.isnumeric():
				self.player_count = int(response)
				is_valid = True
			else:
				print("'{}' is not a whole number.".format(response))

	def add_player(self):
		is_valid = False
		while not is_valid:
			response = input("Please enter your name:\n").strip()
			if response.isalpha():
				self.players.append(Player(response))
				is_valid = True
			else:
				print("'{}' is not a valid name.".format(response))

	def display_instructions(self):
		print("<Insturctions got here>")


	def end_turn(self):
		self.is_game_over()
		self.turn_count += 1

	def is_game_over(self):
		# if game is over set self.is_active to false
		self.is_active = not any(player.score >= self.max_score for player in self.players)



def main():
	game = Game()
	game.run()

if __name__ == '__main__':
	main()
