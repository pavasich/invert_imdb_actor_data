import os, re

# current directory
# place the actor file in the same one
path = os.path.dirname(os.path.abspath(__file__))

FNAME = 'stripped_data.out'

FPATH = os.path.join(path, FNAME)

outf = open(FPATH, 'w')
inf  = open('actors.list', 'r')
regex = re.compile('"|{.*}|\(#.*\)|\(TV\)|\(V\)|\(VG\)|\(\?+.*\)|\(([^0-9^)]+)\)|\[.*\]|<([^>]*)>')
get_actor = re.compile('([A-Z]?[a-z]* ?[A-Z][a-z,]+ ?[A-Z]*[a-z]* ?[A-Z]*[a-z]*)\\t')

# Skip the intro
i = 0
while i < 3852:
    inf.readline()
    i += 1

db = {}

while True:
    line = inf.readline()

    # EOF
    if not line:
        break

    # remove excess characters
    line = regex.sub('', line)

    # check if an actor name is in this line
    actor_maybe = get_actor.match(line)
    
    if actor_maybe:

        # write the previous actor's movies 
        for key in db:       
            outf.write(key + '\n')

        # clear the db
        db = {}

        # Make it easy to see when we encounter a new actor
        outf.write("\nACTOR\n")
        outf.write(actor_maybe.groups()[0] + '\n')

        # sub out the actor
        line = get_actor.sub('', line)


    # clean up the line to get "Movie (year)"
    line = ' '.join(map(lambda word: word.replace('\s', ''), line.split()))

    # save it to this actor's db
    db[line] = 1

# last actor
for key in db:
    outf.write(key + '\n')
    

inf.close()
outf.close()
