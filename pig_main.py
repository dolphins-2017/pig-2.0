import random

class Player:
	def __init__(self, name):
		self.player_name = name
		self.total_score = 0
		self.current_score = 0
		self.status = "Hold"


def dice_sim():
	res_list = []
	for i in range (2):
		res_list.append(random.randrange(1, 6))
	return res_list, sum(res_list)




def main():
	game = True
	player_list = []
	player1 = Player("Player 1")
	player_list.append(player1)
	player2 = Player("Player 2")
	player_list.append(player2)
	player_flag = 1
	bank_flag = 1
	print("Welcome to Pig!")
	score_cap = int(input("Please input a score cap: "))

	while(game):
		result_dice = []
		round_score = 0

		if player_flag == 1:
			player_list[0].status = "Playing"
			player_list[1].status = "Hold"
		elif player_flag == -1:
			player_list[1].status = "Playing"
			player_list[0].status = "Hold"

		player_command = input("Enter r for roll, b for bank:")
		print("\n")
		if player_command == 'r':
			for player in player_list:
				if(player.status == "Playing"):
					bank_flag = 1
					result_dice, round_score = dice_sim()
					player.current_score += round_score
					print(player.player_name, " Result: ",result_dice)
					if(result_dice[0] == result_dice[1]) and (result_dice[0] == "1"):
						print("Snake-eyes!")
						player.total_score = 0
						player.current_score = 0
						player.status = "Hold"
						player_flag = -player_flag
						bank_flag = 1
						print(player.player_name, " total score:", player.total_score)
						print("Switched!\n")
					elif(result_dice[0] == result_dice[1]):
						print("Doubles!")
						bank_flag = 0
						print("Round Score:", round_score)
						print("Current Score:", player.current_score, "\n")
					elif(result_dice[0] == 1) or (result_dice[1] == 1):
						print("Pig!")
						player.current_score = 0
						player.status = "Hold"
						player_flag = -player_flag
						bank_flag = 1
						print(player.player_name, " total score:", player.total_score)
						print("Switched!\n")
					else:
						print("Round Score:", round_score)
						print("Current Score:", player.current_score, "\n") 	
		elif player_command == 'b' and bank_flag == 1:
			for player in player_list:
				if(player.status == "Playing"):
					player.total_score += player.current_score
					print(player.player_name, " total score:", player.total_score)
					player.current_score = 0
					player.status = "Hold"
					player_flag = -player_flag
					print("Switched!\n")
		elif player_command == 'b' and bank_flag == 0:
			print("You cannot bank now, please choose r!")
		print("================================================")
		for player in player_list:
			if player.total_score >= score_cap:
				print("Congratulation!", player.player_name, "wins!")
				game = False

if __name__ == '__main__':
	main()
