####CODE AREA####
import random


#size_start = input("Cube Size: ")
size = 4
#size = int(size_start)

############################################## Nem me pergunte como isso funciona
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

def c(i,j,to): # Modifica um valor na posição (i,j) para 'to'
	row[i-1][j-1] = to 

def fh(choice): # Rotaciona a Face número 'choice' no sentido horário
	if choice > size:
		choice = choice%size
	num = choice-1
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
	if choice > size:
		choice = choice%size
	num = choice-1
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

def td(choice): #Mexe a linha 'choice' para a direita
	if choice > size:
		choice = choice%size
	temp = row[choice-1][-size:]
	row[choice-1][size:] = row[choice-1][:size**2 - size]
	row[choice-1][:size] = temp
	render()

def te(choice): #Mexe a linha 'choice' para a esquerda
	if choice > size:
		choice = choice%size
	temp = row[choice-1][:size]
	row[choice-1][:size**2 - size] = row[choice-1][size:]
	row[choice-1][-size:] = temp
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
### Testing Zone ###

for i in range(size):
	for j in range(size**2):
		c(i+1,j+1,random.randint(0,9))
render()

inp = 0
while inp != "exit":
	inp = input("Command: ")
	do = inp
	try:
		eval(do)
	except:
		print("Invalid Command.")