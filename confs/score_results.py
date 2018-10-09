import importlib
import sys

filename = sys.argv[1]


mod = importlib.import_module(filename)
out = open("%s.txt" % filename)


def valid(cat, blocked) :
    if (cat[0] < 0 or cat[0] > 10 or
        cat[1] < 0 or cat[1] > 10 or
        cat in blocked) :
        return False
    return True

def move(cat, direction, blocked) :
    canditates = []
    
    if cat[0] % 2 == 0 :
        candidates = [
            (cat[0] - 1, cat[1] - 1, "NW"),
            (cat[0] - 1, cat[1],     "NE"),
            (cat[0], cat[1] - 1,     "W"),
            (cat[0], cat[1] + 1,     "E"),
            (cat[0] + 1, cat[1] - 1, "SW"),
            (cat[0] + 1, cat[1],     "SE")
        ]
    else :
        candidates = [
            (cat[0] - 1, cat[1],     "NW"),
            (cat[0] - 1, cat[1] + 1, "NE"),
            (cat[0], cat[1] - 1,     "W"),
            (cat[0], cat[1] + 1,     "E"),
            (cat[0] + 1, cat[1],     "SW"),
            (cat[0] + 1, cat[1]+1,   "SE")
        ]
        
    for el in candidates :
        cand = (el[0], el[1])
        if direction == el[2] and valid(cand, blocked) :
            return cand        
    return None

cat = mod.cat
error = False
steps = 0
for line in out :
    line = line.rstrip()
    if line :
        steps += 1
        cat  = move(cat, line, mod.blocks)
        if not cat :
            error = True
            break

if error :
    print(0)        
elif not cat in mod.exits :
    print(0)
elif steps >= 2*mod.minimum :
    print(0)
else :
    print( (2.0*mod.minimum - steps)/ mod.minimum)


