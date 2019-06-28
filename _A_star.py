import importlib
import sys
import math
from PIL import Image, ImageDraw

blocked = []

def compute_image(cat, blocks, exits):
	im = Image.open("tabuleiro.png").convert("RGBA")
	draw = ImageDraw.Draw(im)

	if type(exits) == list:
		for el in exits:
			shift = el[0] % 2 * 25
			init_x = shift + el[1]*50 + el[1]*5
			end_x = shift + (el[1]+1)*50 + el[1]*5
			init_y = el[0]*49
			end_y = (el[0]+1)*49
			draw.ellipse([init_x, init_y, end_x, end_y],
						fill="blue"
						)
	else:
		for el in [exits]:
			shift = el[0] % 2 * 25
			init_x = shift + el[1]*50 + el[1]*5
			end_x = shift + (el[1]+1)*50 + el[1]*5
			init_y = el[0]*49
			end_y = (el[0]+1)*49
			draw.ellipse([init_x, init_y, end_x, end_y],
                            fill="blue"
                )

	for el in blocks:
		shift = el[0] % 2 * 25
		init_x = shift + el[1]*50 + el[1]*5
		end_x = shift + (el[1]+1)*50 + el[1]*5
		init_y = el[0]*49
		end_y = (el[0]+1)*49
		draw.line([init_x+10, init_y+10, end_x-10, end_y-10],
					fill="red", width=6)
		draw.line([init_x+10, end_y-10, end_x-10, init_y+10],
					fill="red", width=6)

	for el in [cat]:
		shift = el[0] % 2 * 25
		init_x = shift + el[1]*50 + el[1]*5
		end_x = shift + (el[1]+1)*50 + el[1]*5
		init_y = el[0]*49
		end_y = (el[0]+1)*49
		draw.ellipse([init_x, init_y, end_x, end_y],
						fill="black"
						)
	del draw
	return im

def is_valid(player):
    if (player[0] < 0 or player[0] > 10 or
        player[1] < 0 or player[1] > 10 or
        player in blocked):
        return False
    return True

def move(player, direction):
    canditates = []
    if player[0] % 2 == 0:
        candidates = [
            (player[0] - 1, player[1] - 1, "NW"),
            (player[0] - 1, player[1],     "NE"),
            (player[0], player[1] - 1,     "W" ),
            (player[0], player[1] + 1,     "E" ),
            (player[0] + 1, player[1] - 1, "SW"),
            (player[0] + 1, player[1],     "SE")
        ]
    else:
        candidates = [
            (player[0] - 1, player[1],     "NW"),
            (player[0] - 1, player[1] + 1, "NE"),
            (player[0], player[1] - 1,     "W" ),
            (player[0], player[1] + 1,     "E" ),
            (player[0] + 1, player[1],     "SW"),
            (player[0] + 1, player[1]+1,   "SE")
        ]
    for el in candidates:
        cand = (el[0], el[1])
        if direction == el[2] and is_valid(cand):
            return cand
    return False

# Diagonal
def heuristic_3(player, exit):
	dx = abs(player[0] - exit[0])
	dy = abs(player[1] - exit[1])
	return max(dx, dy)

# Manhattan
def heuristic_2(player, exit):
	dx = abs(player[0] - exit[0])
	dy = abs(player[1] - exit[1])
	return dx + dy

#  Euclidean
def heuristic_1(player, exit):
	dx = (player[0] - exit[0])**2
	dy = (player[1] - exit[1])**2
	resultado = math.sqrt((dx + dy))
	return resultado

# Chebyshev
def heuristic(player, exit):
	D = 1
	D2 = 1
	dx = abs(player[0] - exit[0])
	dy = abs(player[1] - exit[1])
	resultado = D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
	return resultado

def neighbourhood(player):
	n = []
	for d in ['E','NE','SE','W','NW','SW']:
		_player = move(player, d)
		if _player:
			n.append(_player)
	return n

def generate_routes(player, exit):

	print('\n\n[@] A* Search\t' + str(player) + '->' + str(exit))

	G = {} 
	F = {}

	G[player] = 0 
	F[player] = heuristic(player, exit)

	open = set([player])
	closed = set()
	trajeto = {}

	while len(open) > 0:

		current = None
		currentF = None

		for pos in open:
			if current is None or F[pos] < currentF:
				currentF = F[pos]
				current = pos

		print('Selected Node :' + str(current))
		
		if current == exit:
			print('[+] Found Route ')
			caminho = [current]
			while current in trajeto:
				current = trajeto[current]
				caminho.append(current)
			caminho.reverse()
			return caminho, len(caminho)-1
 
		open.remove(current)
		closed.add(current)

		print('Checking neighbourhood: ', end='')

		for neighbour in neighbourhood(current):
			if neighbour in closed:
				continue 
				
			candidateG = G[current] + 1
 
			if neighbour not in open:
				open.add(neighbour)
			elif candidateG >= G[neighbour]:
				continue 

			trajeto[neighbour] = current
			G[neighbour] = candidateG
			F[neighbour] = G[neighbour] + heuristic_1(neighbour, exit)

			print('[' + str(neighbour) + ':' + str(F[neighbour]) + ']', end=', ')

		print()
		
	print("[-] A* failed to find a solution")

def create_gif(path):
	images = []
	for step in path:
		images.append(compute_image(step, blocked, saida))
	images[0].save('AStar_' + filename + '-' + str(saida) + '.gif', save_all=True, append_images=images[1:], duration=200, loop=0)

filename = sys.argv[1]

mod = importlib.import_module(filename)

jogador = tuple(mod.cat)
saidas = set(mod.exits)
bloqueados = mod.blocks
minimo = mod.minimum

blocked = bloqueados[:]

rotas = {}

print('[:] Minimum Cost: ' + str(minimo))

# compute_image(jogador, blocked, list(saidas)).save(filename + '.png')

for saida in saidas:
	rota, custo = generate_routes(jogador, saida)
	print('[!] Route Cost: ' + str(custo))
	rotas[custo] = rota
	create_gif(rota)
