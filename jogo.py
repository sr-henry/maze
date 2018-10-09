import importlib
import sys

blocked = []

def valid(player):
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
        if direction == el[2] and valid(cand):
            return cand
    return False

def calcular_heuristica(player, exit):
	dx = abs(player[0] - exit[0])
	dy = abs(player[1] - exit[1])
	resultado = (dx + dy) - min(dx,dy)
	return resultado

def verifica_posicao(player):
	n = []
	for d in ['E','NE','SE','W','NW','SW']:
		_player = move(player, d)
		if _player:
			n.append(_player)
	return n

def gera_rotas(player, exit):
	G = {} 
	F = {}

	G[player] = 0 
	F[player] = calcular_heuristica(player, exit)

	fechados = set()
	abertos = set([player])
	trajeto = {}

	while len(abertos) > 0:
		atual = None
		currentFscore = None
		for pos in abertos:
			if atual is None or F[pos] < currentFscore:
				currentFscore = F[pos]
				atual = pos
 
		if atual == exit:
			caminho = [atual]
			while atual in trajeto:
				atual = trajeto[atual]
				caminho.append(atual)
			caminho.reverse()
			return caminho, F[exit] #Feito!
 
		abertos.remove(atual)
		fechados.add(atual)
 
		for vizinho in verifica_posicao(atual):
			if vizinho in fechados: 
				continue 
			candidateG = G[atual] + 1
 
			if vizinho not in abertos:
				abertos.add(vizinho) 
			elif candidateG >= G[vizinho]:
				continue 
 
			trajeto[vizinho] = atual
			G[vizinho] = candidateG
			H = calcular_heuristica(vizinho, exit)
			F[vizinho] = G[vizinho] + H
			
	raise RuntimeError("A* failed to find a solution")

def mostra_rota(player, rota):
	for r in rota:
		for d in ['E','NE','SE','W','NW','SW']:
			if move(player, d) == r:
				player = move(player, d)
				print(d)

filename = sys.argv[1]

mod = importlib.import_module(filename)
out = open("%s.txt" % filename)

jogador = tuple(mod.cat)
saidas = set(mod.exits)
bloqueados = mod.blocks
minimo = mod.minimum

blocked = bloqueados[:]

rotas = {}

for saida in saidas:
	rota, dist = gera_rotas(jogador, saida)
	rotas[dist] = rota

for key in rotas:
	if key == minimo:
		mostra_rota(jogador, rotas[key])