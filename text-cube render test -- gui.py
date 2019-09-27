####INITIAL SETUP AND SETTINGS AND FUNCTIONS#########

#size_start = input("Cube Size: ")
size = 3
#size = int(size_start)

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

def c(i,j,to):
	row[i-1][j-1] = to 

def fh(choice):
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

def fa(choice):
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

def render(size = size):
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

#render()
####################################################################################
c(1,1,1)
c(1,2,6)
c(1,3,4)
c(3,1,3)
c(3,2,3)
c(3,3,3)
c(3,6,8)
c(1,4,7)
c(1,5,3)
c(1,6,9)
c(1,7,9)
c(1,8,9)
c(1,9,9)
c(2,3,9)
c(3,9,5)
c(3,7,2)
c(2,9,9)
render()

inp = 0
while inp != "exit":
	inp = input("Command: ")
	do = inp
	eval(do)