#Initial Setup and Useful Info
primes_list = [2,3,5,7,11,13]
cube_colours = ['White','Red','Green','Orange','Blue','Yellow']
mix = zip(primes_list,cube_colours)
colour_prime_relation = list(mix)
msg = 'Cube piece is '
print("The following list is the number and its associated colour:")
print(colour_prime_relation)
######################################################################

# Como esse cubo funciona: Cada cor tem um número primo associado, peças de
# multiplas cores é apenas o produto dos números primos associado às cores da
# peça. A lista se diz 'primal' quando contém apenas os números associados.
# A lista se diz 'legível' quando os números foram transformados nas suas
# respectivas cores.

#Função que detecta cor da peça
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

#Mesma utilidade que get_colour, porém retorna apenas a letra inicial da cor
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

#Função que gera as peças centrais (de 1 cor) para um cubo de tamanho qualquer
def gen_centres(cube_size = 3):
	if cube_size <= 1:
		return "Error"
	primes_list = [2,3,5,7,11,13]
	centre_size = cube_size - 2
	centres = primes_list*centre_size**2
	centres.sort()
	return centres

#Função que gera as peças do meio (de 2 cores) para um cubo de tamanho qualquer
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

#Função que gera as peças do canto (de 3 cores) para um cubo de tamanho qualquer
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

#As funções passadas criam algumas peças que não existem (ex: branca e amarela)
#Essa função remove tais peças
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

#Função de teste -- diz a cor das peças sem transformar a lista de primal para legível
def check_colours(cube):
	for i in cube:
		a = short(i)
		print(a)

#Transforma a lista de peças da forma "primal" para forma legível -- não tem como reverter (função de reverter pode ser feita caso necessário)
def transform(cube):
	empty_list = []
	for i in cube:
		a = short(i)
		empty_list.append(a)
	return empty_list

#Função que junta as anteriores para gerar o cubo -- por enquanto gera uma lista unidimensional das peças
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
Cube = gen_cube(3)
print(Cube)
print("we dont know what were doing")
