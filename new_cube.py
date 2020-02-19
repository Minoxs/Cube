#Initial Setup and Useful Info
import random
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
# This is just a bodge to create multiple variables without knowing how many there are beforehand
# This part will create the 'skeleton' of the cube
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
def fh(choice): # Rotates face numbered 'choice' clockwise
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

def fa(choice): # Rotates face numbered 'choice' anti-clockwise
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

def ld(choice): # Moves line 'choice' to the right
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

def le(choice): # Moves line 'choice' to the left
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

def cc(choice): # Rotates a column down -> up (clockwise)
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

def cb(choice): # Rotates a column up -> down (counter-clockwise)
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

def render(size = size): # Renders the 'slices' of the cube separately
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
##########BUILDING THE CUBE##########
# Making use of symmetries and math to build the cube of any size
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
#print("Scramble Moves: ")
#print(scramble_moves)
hold = input("Scramble Finished!")
print("\n"*5)
render()