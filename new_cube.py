import random

class TinyCubeException(Exception): #Error Exception when the cube is too small, more for vanity than anything hihi
	def __init__(self):
		print("Cute little cube!\n")

class WrongMove(Exception): #Error exception when trying to move the cube in wonky ways
	def __init__(self):
		print("The cube doesn't move like that, you silly!\n")

class Cube:
	
	def __init__(self, size): #Initializes and builds cube
		if size <= 1:
			raise TinyCubeException
		self.size = size
		self.pieces = []
		self.playerMoves = []
		self.allMoves = []

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

		self.solvedState = [list(piece) for piece in self.pieces] #Saving solved state to check if cube is solved
		self.isSolved = True

	def __str__(self): #In case I want to print the object
		msg = "This is a size {} cube"
		return msg.format(self.size)

	def __eq__(self, other): #A way of comparing if two cubes are the same :)
		if isinstance(other, Cube):
			return self.pieces == other.pieces
		else:
			return false

	def render(self, toRender): #Renders either the cube or it's logged predecessors
		if toRender == "cube":
			toRender = [self.pieces]

		for rendering in toRender:
			if type(rendering) is str:
				print(rendering)

			else:
				for i in range(self.size):
					line = ""
					count = 0
					for j in rendering[i]:
						if count%self.size == 0:
							line += " |"
						count += 1
						line += " {}".format(j)
					line += " |"
					print(line)
			print("\n")

	def checkChoice(self, choice):
		choice = choice - 1
		if choice < 0 or type(choice) is not int:
			raise WrongMove
		if choice >= self.size:
			choice = choice%self.size
		return choice

	def logMove(self):
		for logList in [self.playerMoves, self.allMoves]:
			temp = []
			for pieces in self.pieces:
				temp.append(list(pieces))
			logList.append(temp)

	def frontClockwise(self, choice): # Rotates face number 'choice' clockwise
		num = self.checkChoice(choice)
		self.logMove()
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
		num = self.checkChoice(choice)
		self.logMove()
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
		choice = self.checkChoice(choice)
		self.logMove()
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
		choice = self.checkChoice(choice)
		self.logMove()
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
		choice = self.checkChoice(choice)
		self.logMove()
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
		choice = self.checkChoice(choice)
		self.logMove()
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

	def scrambleCube(self, amountOfMoves): #Scrambles the cube in a set amount of moves
		self.isSolved = False
		whatRotation = []
		whereToRotate = []
		for i in range(amountOfMoves):
			whatRotation.append(random.randint(1,6))
			whereToRotate.append(random.randint(1,self.size))
		for i in range(len(whatRotation)):
			if whatRotation[i] == 1:
				self.frontClockwise(whereToRotate[i])
				self.allMoves.append('frontClockwise({})'.format(whereToRotate[i]))
			if whatRotation[i] == 2:
				self.frontAntiClockwise(whereToRotate[i])
				self.allMoves.append('frontAntiClockwise({})'.format(whereToRotate[i]))
			if whatRotation[i] == 3:
				self.horizontalRight(whereToRotate[i])
				self.allMoves.append('horizontalRight({})'.format(whereToRotate[i]))
			if whatRotation[i] == 4:
				self.horizontalLeft(whereToRotate[i])
				self.allMoves.append('horizontalLeft({})'.format(whereToRotate[i]))
			if whatRotation[i] == 5:
				self.verticalDown(whereToRotate[i])
				self.allMoves.append('verticalDown({})'.format(whereToRotate[i]))
			if whatRotation[i] == 6:
				self.verticalUp(whereToRotate[i])
				self.allMoves.append('verticalUp({})'.format(whereToRotate[i]))
			del self.playerMoves[-1]

	def checkIfSolved(self):
		if self.pieces == self.solvedState:
			self.isSolved = True
			print("Cube Solved!")
		else:
			print("Keep Trying!")