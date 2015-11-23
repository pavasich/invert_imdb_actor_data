import json, codecs, os

path = os.path.dirname(os.path.abspath(__file__))
inf = os.path.join(path, 'stripped_data.out')
outf = os.path.join(path, 'movie_to_actor.json')

f = codecs.open(inf, 'r', 'latin-1')

db = {}
print 'compiling database...',
while True:
    
    line = f.readline()

    # EOF
    if not line:
        break

    # \n
    line = line.strip()
    if not line:
        continue

    # new actor
    if line == 'ACTOR':
        actor = f.readline().strip()
        continue

    # lazy
    try:
        db[line][actor] = 1
    except:
        db[line] = { actor: 1 }
        
f.close()

print 'finished!'
print 'organizing...',

# {actorA: 1, actorB: 2, ...} => [actorA, actorB, ...]
for movie in db:
    db[movie] = { 'actors': db[movie].keys() }

print 'finished!'
print 'dumping json...',

# The dump!
with codecs.open(outf, 'w', 'utf-8') as out:
    json.dump(db, out, indent=4, ensure_ascii=False)
print 'done!'
