#Initial Setup and Useful Info
lb = "\n"
import random
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
#Initial Setup and Useful Info
import random
from pathlib import Path as find

###############################################
# Main Menu
menu = 1
def menu():
	print("""
		#====================#
		#  1 - Start Game	 #
		#  2 - Options	     #
		#  3 - Instructions  #
		#  4 - Exit 		 #
		#====================#
		""")
	while menu == 1:
		inp = input("")
###############################################
###############################################
# Settings

###############################################


size = 0
while size < 1:
	size_start = input("Cube Size: ")
	try:
		size = int(size_start)
	except:
		size_start = input("Cube Size: ")
############################################## 
#Special Size Case
if size == 1:
	print("Cute little cube!")
	print("Already finished, congratulations :)")
	hold = input("ENTER to close.")
	exit()
##############################################
# Nem me pergunte como isso funciona
# Essa parte é encarregada de gerar o 'esqueleto' do cubo
def create_row(size):
	row = [0 for i in range(size)]
	return row

def row_nums(size):
	row_n = [i for i in range(size)]
	a = zip(row_n,row_n)
	return a

def dict(size):
	lst = row_nums(size)
	rows = {row:wor for row, wor in lst}
	return rows

row = dict(size)
for i in range(size):
	row[i] = create_row(size**2)	
###############################################
def fh(choice): # Rotaciona a Face número 'choice' no sentido horário
	choice = choice - 1
	if choice < 0:
		print("Invalid Choice.")
		return 0
	if choice >= size:
		choice = choice%size
	num = choice
	tb = range(num*size,size+num*size)
	m = range(0,size)
	t = [row[0][i] for i in tb]
	l = [row[i][num*size] for i in m]
	r = [row[i][size-1+num*size] for i in m]
	b = [row[size-1][i] for i in tb]
	
	j = -1
	for i in range(len(t)):
		row[m[i]][size-1+num*size] = t[i]
		row[size-1][tb[i]] = r[j]
		row[m[i]][num*size] = b[i]
		row[0][tb[i]] = l[j]
		j += -1
	render()

def fa(choice): # Rotaciona a Face número 'choice' no sentido anti-horário
	choice = choice - 1
	if choice < 0:
		print("Invalid Choice.")
		return 0
	if choice >= size:
		choice = choice%size
	num = choice
	tb = range(num*size,size+num*size)
	m = range(0,size)
	t = [row[0][i] for i in tb]
	l = [row[i][num*size] for i in m]
	r = [row[i][size-1+num*size] for i in m]
	b = [row[size-1][i] for i in tb]

	j = -1
	for i in range(len(t)):
		row[m[i]][size-1+num*size] = b[j]
		row[size-1][tb[i]] = l[i]
		row[m[i]][num*size] = t[j]
		row[0][tb[i]] = r[i]
		j += -1
	render()

def ld(choice): #Mexe a linha 'choice' para a direita
	choice = choice - 1
	if choice < 0:
		print("Invalid Choice.")
		return 0
	if choice >= size:
		choice = choice%size
	temps = []
	for i in range(size):
		temp2 = []
		for j in range(size):
			temp2.append(row[choice][j+(i*size)])
		temps.append(temp2)
	k = 0
	for i in range(size):
		load = temps[i]
		for j in range(size):
			row[choice][(size-1)+(j*size)-k] = load[j]
		k += 1
	render()

def le(choice): #Mexe a linha 'choice' para a esquerda
	choice = choice - 1
	if choice < 0:
		print("Invalid Choice.")
		return 0
	if choice >= size:
		choice = choice%size
	temps = []
	for i in range(size):
		temp2 = []
		for j in range(size):
			temp2.append(row[choice][j+(i*size)])
		temps.append(temp2)
	
	for i in range(size):
		load = temps[i]
		k = 1
		for j in range(size):
			row[choice][(j*size)+i] = load[-k]
			k += 1
	render()

def cc(choice): #Rotate a column down -> up (clockwise)
	choice = choice - 1
	if choice < 0:
		print("Invalid Choice.")
		return 0
	if choice >= size:
		choice = choice%size
	temps = []
	for i in range(size):
		temp2 = []
		for j in range(size):
			temp2.append(row[j][(choice)+(size*i)])
		temps.append(temp2)
	for i in range(size):
		k = 1
		load = temps[i]
		for j in range(size):
			row[i][choice+(size*j)] = load[-k]
			k += 1
	render()

def cb(choice): #Rotate a column up -> down (counter-clockwise)
	choice = choice - 1
	if choice < 0:
		print("Invalid Choice.")
		return 0
	if choice >= size:
		choice = choice%size
	temps = []
	for i in range(size):
		temp2 = []
		for j in range(size):
			temp2.append(row[j][(choice)+(size*i)])
		temps.append(temp2)
	for i in range(size):
		load = temps[-(i+1)]
		for j in range(size):
			row[i][choice+(size*j)] = load[j]
	render()

def render(size = size): #Renderiza os 'slices' do cubo separadamente
	print("\n"*5)
	for i in range(size):
		line = ""
		count = 0
		for j in row[i]:
			if count%size == 0:
				line += " |"
			count += 1
			line += " {}".format(j)
		line += " |"
		print(line)
####################################################################################
##########CONSTRUINDO O CUBO##########
#
l = size-1
row[0][0] = "RYB"
row[1][0] = "R_B"
row[l][0] = "RWB"
for i in range(1,size-1):
	row[0][i] = "R_Y"
	row[1][i] = "_R_"
	row[l][i] = "R_W"
row[0][size-1] = "RYG"
row[1][size-1] = "R_G"
row[l][size-1] = "RWG"
row[0][size] = "Y_B"
row[1][size] = "_B_"
row[l][size] = "W_B"
for i in range(size+1,size*2):
	row[0][i] = "_Y_"
	row[1][i] = "000"
	row[l][i] = "_W_"
row[0][size*2-1] = "Y_G"
row[1][size*2-1] = "_G_"
row[l][size*2-1] = "W_G"
row[0][size**2-size] = "OYB"
row[1][size**2-size] = "O_B"
row[l][size**2-size] = "OWB"
for i in range(size**2-size+1,size**2):
	row[0][i] = "O_Y"
	row[1][i] = "_O_"
	row[l][i] = "O_W"
row[0][size**2-1] = "OYG"
row[1][size**2-1] = "O_G"
row[l][size**2-1] = "OWG"
row[0][size*2:size**2-size] = row[0][size:size*2]*(size-3)
row[1][size*2:size**2-size] = row[1][size:size*2]*(size-3)
row[l][size*2:size**2-size] = row[l][size:size*2]*(size-3)
for i in range(2,size-1):
	k = 0
	for c in row[1]:
		row[i][k] = c
		k += 1
row[size-1][size*2:size**2-size] = row[size-1][size:size*2]*(size-3)
#
render()
###########################################################################
# Saving solved cube
solved = []
for i in range(size):
	for j in range(size**2):
		solved.append(row[i][j])
###########################################################################
###########################################################################
scramble_moves = []
# Scrambling Cube
hold = input("Starting Scramble...")
moves = []
move_row = []
for i in range(size**3):
	moves.append(random.randint(1,6))
	move_row.append(random.randint(1,size))
for i in range(len(moves)):
	if moves[i] == 1:
		fh(move_row[i])
		scramble_moves.append('fh({})'.format(move_row[i]))
	if moves[i] == 2:
		fa(move_row[i])
		scramble_moves.append('fa({})'.format(move_row[i]))
	if moves[i] == 3:
		le(move_row[i])
		scramble_moves.append('le({})'.format(move_row[i]))
	if moves[i] == 4:
		ld(move_row[i])
		scramble_moves.append('ld({})'.format(move_row[i]))
	if moves[i] == 5:
		cc(move_row[i])
		scramble_moves.append('cc({})'.format(move_row[i]))
	if moves[i] == 6:
		cb(move_row[i])
		scramble_moves.append('cb({})'.format(move_row[i]))
print("\n"*10)
print("Starting position is: Red Face in front, Yellow face on top")
print("Scramble Moves: ")
print(scramble_moves)
hold = input("Scramble Finished!")
print("\n"*5)
render()
#
###########################################################################
# Taking Commands
command = 0
while command != "exit":
	com = input("Choose a move: ")
	try:
		command = com.lower()
	except:
		continue
	if command == "r":
		cc(size)
	elif command == "r'":
		cb(size)
	elif command == "l":
		cb(1)
	elif command == "l'":
		cc(1)
	elif command == "b":
		fa(size)
	elif command == "b'":
		fh(size)
	elif command == "d":
		ld(size)
	elif command == "d'":
		le(size)
	elif command == "f":
		fh(1)
	elif command == "f'":
		fa(1)
	elif command == "u":
		le(1)
	elif command == "u'":
		ld(1)
	elif command == "y":
		for i in range(size):
			le(i+1)
	elif command == "y'":
		for i in range(size):
			ld(i+1)
	elif command == "x":
		for i in range(size):
			cb(i+1)
	elif command == "x'":
		for i in range(size):
			cc(i+1)
	elif command == "solved":
		check = 0
		mistakes = []
		for i in range(size):
			for j in range(size**2):
				if row[i][j] == solved[j+i*size**2]:
					check += 1
				else:
					mistakes.append((i+1,j+1))
		if check == size**3:
			print("Congratulations!!!")
			print("You solved the cube!")
			hold = input("Press ENTER to close.")
			exit()
		else:
			print("Keep trying!")
			print(mistakes)
	else:
		try:
			eval(command)
		except:
			print("Invalid Command.")
			continue
###########################################################################