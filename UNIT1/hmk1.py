sensor_wrong = 1.0 - sensor_right
p_stay = 1.0 - p_move

def sense(p, colors, measurement):
	aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
	s = 0.0
	for i in range(len(p)):
		for j in range(len(p[i])):
			hit = (measurement == colors[i][j]
			aux[i][j] = p[i][j] * (hit * sensor_right + (1-hit) * sensor_wrong
			s += aux[i][j]
	for i in range(len(aux)):
		for j in range(len(p[i])):
			aux[i][j] /= s
	return aux
	
def move(p,motion):
	aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
	
	for i in range(len(p)):
		for j in range(len(p[i])):
			aux[i][j] = (p_move * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])]) + (p_stay * p[i][j])
			
	return aux	
	
#inicia vetor de probabilidades iniciais 
pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors[0]))]

for k in range(len(measurements)):
	p = move(p,motions[k])
	p = sense(p, colors, measurements[k])