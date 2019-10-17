#Initial Setup and Useful Info
lb = "\n"
import platform
import datetime
from pathlib import Path as find
error_msg = "Something went Wrong!"
#Função que detecta e diz o sistema quando compilado
def os_detect():
	sys = platform.system()
	plt = platform.release()
	os_name = "{} {}".format(sys,plt)
	print("Sistema Operacional: "+os_name)

os_detect()

#Função que define aonde será salvo logs
def set_filepath(save_to = "not_set"):
	saving = str(find.cwd())
	return saving

filepath = set_filepath()
print("Pasta atual: "+filepath)

time_now = datetime.datetime.now()
print("Data: "+str(time_now))

############################################################################################
#Basic Functions############################################################################
#Adiciona o que acontece em um .txt

def printer(add_to_log, title = "log", mode = "a+", extension = ".txt"):
	path = "{}{}{}".format(filepath,title,extension)
	p = open(path, mode)
	p.write(str(add_to_log) + lb)
	p.close()
############################################################################################
###############################################
# Main Menu
def menu():
	menu = 1
	menu_msg =		"""
					#====================#
					#  1 - Start Game    #
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
			import cube
			cube.render()
			cube.commands()
			print(menu_msg)
		elif inp == 2:
			print("Load Function TBA")
		elif inp == 3:
			options()
		elif inp == 4:
			print("Instructions TBA")
		elif inp == 5:
			print("Thanks for playing!")
			exit()
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