handle = open('routes.txt')
routes ={}
for line in handle:
	line = line.strip()
	words = line.split('::')
	#print words[0], words[1]
	routes[words[0]] = words[1]
handle.close()

handle = open('ratings.txt')
ratings={}
i=0
for line in handle:
	line=line.strip()
	words=line.split('::')
	if words[0] not in ratings:
		ratings[words[0]] = {routes[words[1]]:float(words[2])}
	else:
		ratings[words[0]][routes[words[1]]] = float(words[2])
	#if i > 100:
	#	break
	i = i+1
print ratings
