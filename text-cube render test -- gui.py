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

def r(choice):
	num = choice-1
	tb = range(num*size,size+num*size)
	m = range(0,size)
	t = [row[0][i] for i in tb]
	print(t)
	l = [row[i][num*size] for i in m]
	print(l)
	r = [row[i][size-1+num*size] for i in m]
	print(r)
	b = [row[size-1][i] for i in tb]
	print(b)

def render(size = size):
	for i in range(size):
		print(row[i])

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
c(3,9,2)
c(3,7,2)
c(2,9,9)
render()
r(3)

inp = 0
while inp != "exit":
	do = input("Command: ")
	eval(do)