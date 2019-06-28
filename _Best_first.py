import importlib
import sys
import math
from PIL import Image, ImageDraw

blocked = []

def compute_image(cat, blocks, exits):
	im = Image.open("tabuleiro.png").convert("RGBA")
	draw = ImageDraw.Draw(im)

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

visited = set()

bf_path = []

def generate_routes(player, exit):

	F = {}

	current = player

	print('Current Node: ' + str(current))
	
	bf_path.append(current)

	if current == exit:
		return True

	visited.add(current)

	neighbours = []

	for n in neighbourhood(current):
		if n in visited:
			continue
		neighbours.append(n)
		F[n] = heuristic_1(n, exit)
	
	if neighbours:
		print('Checking neighbourhood: ' + str(F))
		for el in sorted(F.items(), key=lambda t: t[1]):
			if not generate_routes(el[0], exit):
				continue
			else:
				return True
	else:
		print('Backtracking...')
		return False
	
	return False


def create_gif(path, exit):
	images = []
	for step in path:
		images.append(compute_image(step, blocked, exit))
	images[0].save('BestFirst_' + filename + '-' + str(saida) + '.gif', save_all=True,
	               append_images=images[1:], duration=200, loop=0)

filename = sys.argv[1]

mod = importlib.import_module(filename)

jogador = tuple(mod.cat)
saidas = set(mod.exits)
bloqueados = mod.blocks
minimo = mod.minimum

blocked = bloqueados[:]

rotas = {}

print('[:] Minimum Cost: ' + str(minimo))

for saida in saidas:
	print('\n\n[@] BestFirst\t' + str(jogador) + '->' + str(saida))
	if generate_routes(jogador, saida):
		print('[+] Found Route\n[!] Route Cost:' + str(len(bf_path)-1))
		create_gif(bf_path, saida)
	else:
		print('[-] BestFirst failed to find a solution')
	bf_path.clear()
	visited.clear()
	#rotas[custo] = rota
