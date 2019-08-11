size_start = input("Cube Size: ")
size = int(size_start)
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

a = dict(size)
for i in range(size):
	a[i] = create_row(size)	

class Row:
	def row(self,size):
		row = [0 for i in range(size)]
		return row


