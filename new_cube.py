class tinyCubeException(Exception): #Error Exception when the cube is too small, more for vanity than anything hihi
	def __init__(self):
		print("Cute little cube!\n")

class wrongMove(Exception): #Error exception when trying to move the cube in wonky ways
	def __init__(self):
		print("The cube doesn't move like that, you silly!\n")

class Cube:
	
	def __init__(self, size): #Initializes and builds cube
		if size <= 1:
			raise tinyCubeException
		self.size = size
		self.pieces = []
		
		self.solvedState = list(self.pieces) #Saving solved state to check if cube is solved
		self.isSolved = True

		#Start of cube-building process
		#Making use of symmetries and math to build the cube of any size
		for i in range(size):
			row = [0 for j in range(size**2)]
			self.pieces.append(row)

		l = size-1
		self.pieces[0][0] = "RYB"
		self.pieces[1][0] = "R_B"
		self.pieces[l][0] = "RWB"
		for i in range(1,size-1):
			self.pieces[0][i] = "R_Y"
			self.pieces[1][i] = "_R_"
			self.pieces[l][i] = "R_W"
		self.pieces[0][size-1] = "RYG"
		self.pieces[1][size-1] = "R_G"
		self.pieces[l][size-1] = "RWG"
		self.pieces[0][size] = "Y_B"
		self.pieces[1][size] = "_B_"
		self.pieces[l][size] = "W_B"
		for i in range(size+1,size*2):
			self.pieces[0][i] = "_Y_"
			self.pieces[1][i] = "000"
			self.pieces[l][i] = "_W_"
		self.pieces[0][size*2-1] = "Y_G"
		self.pieces[1][size*2-1] = "_G_"
		self.pieces[l][size*2-1] = "W_G"
		self.pieces[0][size**2-size] = "OYB"
		self.pieces[1][size**2-size] = "O_B"
		self.pieces[l][size**2-size] = "OWB"
		for i in range(size**2-size+1,size**2):
			self.pieces[0][i] = "O_Y"
			self.pieces[1][i] = "_O_"
			self.pieces[l][i] = "O_W"
		self.pieces[0][size**2-1] = "OYG"
		self.pieces[1][size**2-1] = "O_G"
		self.pieces[l][size**2-1] = "OWG"
		self.pieces[0][size*2:size**2-size] = self.pieces[0][size:size*2]*(size-3)
		self.pieces[1][size*2:size**2-size] = self.pieces[1][size:size*2]*(size-3)
		self.pieces[l][size*2:size**2-size] = self.pieces[l][size:size*2]*(size-3)
		for i in range(2,size-1):
			k = 0
			for c in self.pieces[1]:
				self.pieces[i][k] = c
				k += 1
		self.pieces[size-1][size*2:size**2-size] = self.pieces[size-1][size:size*2]*(size-3)
		#End of cube-building process

	def __str__(self): #In case I want to print the object
		msg = "This is a size {} cube"
		return msg.format(self.size)

	def __eq__(self, other): #A way of comparing if two cubes are the same :)
		if isinstance(other, Cube):
			return self.pieces == other.pieces
		else:
			return false

	def render(self): # Renders the 'slices' of the cube separately
		for i in range(self.size):
			line = ""
			count = 0
			for j in self.pieces[i]:
				if count%self.size == 0:
					line += " |"
				count += 1
				line += " {}".format(j)
			line += " |"
			print(line)

	def frontClockwise(self, choice): # Rotates face number 'choice' clockwise
		choice = choice - 1
		if choice < 0:
			print("Invalid Choice.")
			return 0
		if choice >= self.size:
			choice = choice%self.size
		num = choice
		tb = range(num*self.size,self.size+num*self.size)
		m = range(0,self.size)
		t = [self.pieces[0][i] for i in tb]
		l = [self.pieces[i][num*self.size] for i in m]
		r = [self.pieces[i][self.size-1+num*self.size] for i in m]
		b = [self.pieces[self.size-1][i] for i in tb]
		
		j = -1
		for i in range(len(t)):
			self.pieces[m[i]][self.size-1+num*self.size] = t[i]
			self.pieces[self.size-1][tb[i]] = r[j]
			self.pieces[m[i]][num*self.size] = b[i]
			self.pieces[0][tb[i]] = l[j]
			j += -1

	def frontAntiClockwise(self, choice): # Rotates face number 'choice' anti-clockwise
		choice = choice - 1
		if choice < 0:
			print("Invalid Choice.")
			return 0
		if choice >= self.size:
			choice = choice%self.size
		num = choice
		tb = range(num*self.size,self.size+num*self.size)
		m = range(0,self.size)
		t = [self.pieces[0][i] for i in tb]
		l = [self.pieces[i][num*self.size] for i in m]
		r = [self.pieces[i][self.size-1+num*self.size] for i in m]
		b = [self.pieces[self.size-1][i] for i in tb]

		j = -1
		for i in range(len(t)):
			self.pieces[m[i]][self.size-1+num*self.size] = b[j]
			self.pieces[self.size-1][tb[i]] = l[i]
			self.pieces[m[i]][num*self.size] = t[j]
			self.pieces[0][tb[i]] = r[i]
			j += -1
		
	def horizontalRight(self, choice): # Moves line 'choice' to the right
		choice = choice - 1
		if choice < 0:
			print("Invalid Choice.")
			return 0
		if choice >= self.size:
			choice = choice%self.size
		temps = []
		for i in range(self.size):
			temp2 = []
			for j in range(self.size):
				temp2.append(self.pieces[choice][j+(i*self.size)])
			temps.append(temp2)
		k = 0
		for i in range(self.size):
			load = temps[i]
			for j in range(self.size):
				self.pieces[choice][(self.size-1)+(j*self.size)-k] = load[j]
			k += 1

	def horizontalLeft(self, choice): # Moves line 'choice' to the left
		choice = choice - 1
		if choice < 0:
			print("Invalid Choice.")
			return 0
		if choice >= self.size:
			choice = choice%self.size
		temps = []
		for i in range(self.size):
			temp2 = []
			for j in range(self.size):
				temp2.append(self.pieces[choice][j+(i*self.size)])
			temps.append(temp2)
		
		for i in range(self.size):
			load = temps[i]
			k = 1
			for j in range(self.size):
				self.pieces[choice][(j*self.size)+i] = load[-k]
				k += 1

	def verticalUp(self, choice): # Rotates a column down -> up (clockwise)
		choice = choice - 1
		if choice < 0:
			print("Invalid Choice.")
			return 0
		if choice >= self.size:
			choice = choice%self.size
		temps = []
		for i in range(self.size):
			temp2 = []
			for j in range(self.size):
				temp2.append(self.pieces[j][(choice)+(self.size*i)])
			temps.append(temp2)
		for i in range(self.size):
			k = 1
			load = temps[i]
			for j in range(self.size):
				self.pieces[i][choice+(self.size*j)] = load[-k]
				k += 1

	def verticalDown(self, choice): # Rotates a column up -> down (counter-clockwise)
		choice = choice - 1
		if choice < 0:
			print("Invalid Choice.")
			return 0
		if choice >= self.size:
			choice = choice%self.size
		temps = []
		for i in range(self.size):
			temp2 = []
			for j in range(self.size):
				temp2.append(self.pieces[j][(choice)+(self.size*i)])
			temps.append(temp2)
		for i in range(self.size):
			load = temps[-(i+1)]
			for j in range(self.size):
				self.pieces[i][choice+(self.size*j)] = load[j]