#Standard UI Placeholder
# Main Menu
def menu():
	menu = 1
	menu_msg =		"""
					#====================#
					#  1 - New Game      #
					#  2 - Load Game     #
					#  3 - Cube Options  #
					#  4 - Instructions  #
					#  5 - Exit          #
					#====================#
					"""
	print(menu_msg)
	while menu == 1:
		inp = input("What do:")
		try:
			inp = int(inp)
		except:
			print("Invalid Command!")
			continue
		if inp == 1:
			size = "null"
			while type(size) is not int:
				size = input("Cube Size: ")
				try:
					size = int(size)
				except:
					print("Invalid Input")

			newGame(inp)
		elif inp == 2:
			print("Load Function TBA")
		elif inp == 3:
			options()
		elif inp == 4:
			print("Instructions TBA")
		elif inp == 5:
			print("Thanks for playing!")
			exit()
#New Game
def newGame(size):
	print("baan")

# Load Menu (TBA)

# Options Menu
def options():
	options = 1
	print("""
			#=================================#
			#  1 - Turn Auto-Scramble On/Off  #
			#  2 - Load Seed                  #
			#  3 - Change Render Mode         #
			#=================================#
		""")
# Instructions (TBA)
###############################################
###############################################
# Settings (TBA)

###############################################
menu()