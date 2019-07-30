primes_list = [2,3,5,7,11,13]
cube_colours = ['White','Red','Green','Orange','Blue','Yellow']
mix = zip(primes_list,cube_colours)
colour_prime_relation = list(mix)
msg = 'Cube piece is '
print("The following list is the number and its associated colour:")
print(colour_prime_relation)

def get_colour(cube_piece):
	piece_colour = ' '
	if cube_piece%2 == 0:
		piece_colour += 'White, '
	if cube_piece%3 == 0:
		piece_colour += 'Red, '
	if cube_piece%5 == 0:
		piece_colour += 'Green, '
	if cube_piece%7 == 0:
		piece_colour += 'Orange, '
	if cube_piece%11 == 0:
		piece_colour += 'Blue, '
	if cube_piece%13 == 0:
		piece_colour += 'Yellow, '
	piece_colour_final = piece_colour[1:-2]+'.'
	final = msg + piece_colour_final
	return final

def short(cube_piece):
	piece_colour = ' '
	if cube_piece%2 == 0:
		piece_colour += 'W'
	if cube_piece%3 == 0:
		piece_colour += 'R'
	if cube_piece%5 == 0:
		piece_colour += 'G'
	if cube_piece%7 == 0:
		piece_colour += 'O'
	if cube_piece%11 == 0:
		piece_colour += 'B'
	if cube_piece%13 == 0:
		piece_colour += 'Y'
	piece_colour_final = piece_colour[1:]
	final = piece_colour_final
	return final

def gen_centres(cube_size = 3):
	if cube_size <= 1:
		return "Error"
	primes_list = [2,3,5,7,11,13]
	centre_size = cube_size - 2
	centres = primes_list*centre_size**2
	centres.sort()
	return centres

def gen_edges(cube_size = 3):
	if cube_size <= 1:
		return "Error"
	primes_list = [2,3,5,7,11,13]
	centres = primes_list
	edge_pieces = []
	size = cube_size-2
	for i in centres:
		var = i
		mult = list(range(len(centres)))
		mult_slice = mult[centres.index(i):]
		for h in mult_slice:
			var2 = centres[h]
			if var == var2:
				continue
			else:
				piece = var*var2
				edge_pieces.append(piece)
	final = edge_pieces*size
	return final

def gen_corners(cube_size = 3):
	if cube_size <= 1:
		return "Error"
	primes_list = [2,3,5,7,11,13]
	centres = primes_list
	edges = gen_edges()
	corner_pieces = []
	for i in edges:
		var = i
		for h in primes_list:
			var2 = h
			inx = edges.index(i)
			inx2 = primes_list.index(h)
			if var == var2:
				continue
			if edges[inx]%primes_list[inx2]==0:
				continue
			piece = var*var2
			if piece in corner_pieces:
				continue
			corner_pieces.append(piece)
	return corner_pieces

def remove_impossible_pieces(func, cube_size = 3):
	lst = func
	new_list = []
	for i in lst:
		if i%5==0 and i%11==0:
			continue
		if i%2==0 and i%13==0:
			continue
		if i%3==0 and i%7==0:
			continue
		new_list.append(i)
	return new_list

def check_colours(cube):
	for i in cube:
		a = short(i)
		print(a)

def transform(cube):
	empty_list = []
	for i in cube:
		a = short(i)
		empty_list.append(a)
	return empty_list

def gen_cube(cube_size = 3):
	if cube_size <= 1:
		print("Cube Size Error")
		return "Cube Size Error"
	centres = gen_centres(cube_size)
	edge_pieces = remove_impossible_pieces(gen_edges(cube_size))
	corner_pieces = remove_impossible_pieces(gen_corners(cube_size))
	cube1 = centres + edge_pieces + corner_pieces
	cube = transform(cube1)
	return cube


##The piece order doesn't matter for now - Position and Permutations TBA
Cube = gen_cube(4)
print(Cube)

